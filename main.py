import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests
import pyupbit

access_key = "zH0Ce60M0F6dxgeLbxGqZWjUPfSBd41Kmdl61DYJ"
secret_key = "y6MbRwrFFZyTxu9xNkx5lShe0xexpQcZRJ6R8anL"
server_url = "https://api.upbit.com"
payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

tickers = pyupbit.get_tickers()
print("Tickers :\n", tickers)
upbit = pyupbit.Upbit(access_key, secret_key)
print("Account :\n", upbit.get_balances())
print("bit coin 현재가 :\n", pyupbit.get_current_price("KRW-BTC"))
orders = upbit.get_order('KRW-BTC','done')
print("거래내역:")
for order in orders:
    print(order)
