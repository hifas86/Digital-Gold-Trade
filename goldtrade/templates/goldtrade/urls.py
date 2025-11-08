from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('buy/real/', views.buy_gold, {'is_demo': False}, name='buy_gold_real'),
    path('sell/real/', views.sell_gold, {'is_demo': False}, name='sell_gold_real'),
    path('buy/demo/', views.buy_gold, {'is_demo': True}, name='buy_gold_demo'),
    path('sell/demo/', views.sell_gold, {'is_demo': True}, name='sell_gold_demo'),
]
