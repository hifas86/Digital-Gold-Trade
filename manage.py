#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gold_trade.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# python manage.py shell
from collections import defaultdict
from decimal import Decimal
from goldtrade.models import Wallet, Transaction

seen = set()
dups = []

for w in Wallet.objects.order_by('user_id', 'is_demo', 'id'):
    key = (w.user_id, w.is_demo)
    if key in seen:
        dups.append(w)
    else:
        seen.add(key)

for w in dups:
    keep = Wallet.objects.filter(user_id=w.user_id, is_demo=w.is_demo).order_by('id').first()
    if keep and keep.id != w.id:
        # move transactions
        Transaction.objects.filter(wallet=w).update(wallet=keep)
        # sum balances
        keep.cash_balance += w.cash_balance
        keep.gold_balance += w.gold_balance
        keep.save()
        w.delete()

print("Done. Kept unique wallets.")
