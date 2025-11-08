from django.shortcuts import render
from django.http import JsonResponse
from .models import GoldRate

def gold_price_history(request):
    data = GoldRate.objects.order_by('-last_updated')[:30]  # last 30 records

    formatted = [
        {
            "date": rate.last_updated.strftime("%Y-%m-%d %H:%M"),
            "buy": float(rate.buy_rate),
            "sell": float(rate.sell_rate)
        }
        for rate in data[::-1]
    ]

    return JsonResponse(formatted, safe=False)
