from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class GoldRate(models.Model):
    price_per_gram = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Current Rate: {self.price_per_gram} per gram"


class GoldWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gold_balance = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - {self.gold_balance}g"


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE)
    gold_amount = models.DecimalField(max_digits=10, decimal_places=3)
    price_per_gram = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} {self.gold_amount}g"


class DemoAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    demo_gold = models.DecimalField(max_digits=10, decimal_places=3, default=10.000)
    demo_cash = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Demo: {self.user.username} ({self.demo_gold}g)"