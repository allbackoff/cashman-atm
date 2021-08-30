from rest_framework.test import APITestCase

from rest_framework import status

from .models import Session


class DepositTestCase(APITestCase):
    def setUp(self):
        self.session = Session.objects.create(D_HUNDRED=4, D_TEN=2)

    def test_deposit(self):
        data = {"D_HUNDRED": 3, "D_TWENTY": 5}
        correct_balance = {"D_HUNDRED": 7,
                           "D_FIFTY": 0,
                           "D_TWENTY": 5,
                           "D_TEN": 2,
                           "C_FIFTY": 0,
                           "C_TWENTY": 0,
                           "C_TEN": 0,
                           "C_FIVE": 0
                           }

        response = self.client.post("/atm/deposit/", data)
        response.data.pop('id', None)

        self.assertEqual(response.data, correct_balance)


class WithdrawTestCase(APITestCase):
    def setUp(self):
        self.session = Session.objects.create(D_FIFTY=3, D_TWENTY=8)

    def test_20(self):
        data = {"withdraw_amount": 20}
        correct_combination = {"D_TWENTY": 1}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_40(self):
        data = {"withdraw_amount": 40}
        correct_combination = {"D_TWENTY": 2}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_50(self):
        data = {"withdraw_amount": 50}
        correct_combination = {"D_FIFTY": 1}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_70(self):
        data = {"withdraw_amount": 70}
        correct_combination = {"D_FIFTY": 1, "D_TWENTY": 1}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_80(self):
        data = {"withdraw_amount": 80}
        correct_combination = {"D_TWENTY": 4}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_100(self):
        data = {"withdraw_amount": 100}
        correct_combination = {"D_FIFTY": 2}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_150(self):
        data = {"withdraw_amount": 150}
        correct_combination = {"D_FIFTY": 3}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_60(self):
        data = {"withdraw_amount": 60}
        correct_combination = {"D_TWENTY": 3}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_110(self):
        data = {"withdraw_amount": 110}
        correct_combination = {"D_FIFTY": 1, "D_TWENTY": 3}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

    def test_200(self):
        data = {"withdraw_amount": 200}
        correct_combination = {"D_FIFTY": 2, "D_TWENTY": 5}

        response = self.client.post("/atm/withdraw/", data)

        self.assertEqual(response.data, correct_combination)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
