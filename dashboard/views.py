from django.shortcuts import render
from django.db.models import Sum
from .models import Transaction

def dashboard(request):
    total_buy = Transaction.objects.filter(type="BUY").aggregate(Sum("gold_grams"))["gold_grams__sum"] or 0
    total_sell = Transaction.objects.filter(type="SELL").aggregate(Sum("gold_grams"))["gold_grams__sum"] or 0
    gold_balance = total_buy - total_sell

    return render(request, "dashboard.html", {
        "total_buy": round(total_buy,2),
        "total_sell": round(total_sell,2),
        "gold_balance": round(gold_balance,2)
    })

