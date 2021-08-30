from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SessionSerializer
from .models import Session
from .services import process_deposit, process_withdrawal, get_withdrawal_combination


@api_view(['GET'])
def api_routes(request):
    routes = {
        "/atm/balance": "Check how much of each note present in the current session",
        "/atm/start": "Initialize the ATM with custom combination of banknotes",
        "/atm/deposit": "Deposit the banknotes",
        "/atm/withdraw": "Withdraw money from ATM"
    }

    return Response(routes)


@api_view(['GET'])
def show_balance(request):
    try:
        session = Session.objects.latest('id')
        serializer = SessionSerializer(session)

        return Response(serializer.data)
    except Session.DoesNotExist:
        return Response("No session initialized yet!", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_session(request):
    serializer = SessionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def deposit(request):
    session = Session.objects.latest('id')
    new_balance = process_deposit(request.data, session.__dict__)
    serializer = SessionSerializer(session, data=new_balance, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def withdraw(request):
    withdraw_amount = int(request.data["withdraw_amount"])
    banknotes_combination = {}

    session = Session.objects.latest('id')
    transaction_valid = get_withdrawal_combination(
        withdraw_amount, session.__dict__, banknotes_combination)

    if transaction_valid:
        new_balance = process_withdrawal(
            banknotes_combination, session.__dict__)
        serializer = SessionSerializer(session, data=new_balance, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(banknotes_combination, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response('Error: transaction not valid!', status=status.HTTP_400_BAD_REQUEST)
