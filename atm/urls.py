from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_routes),
    path('balance/', views.show_balance),
    path('start/', views.create_session),
    path('deposit/', views.deposit),
    path('withdraw/', views.withdraw)
]
