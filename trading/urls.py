from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('gold-history/', views.gold_price_history, name='gold_history'),
]
