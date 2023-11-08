# TD Ameritrade Function Library.
# T. Lockman
# August 2021
# O_o tHe pAcKeTs nEvEr LiE, tHe ExEcUtIvEs AlWaYs Do o_O #


import requests
import json
import pandas as pd

td_consumer_key = 'enter consumer key here'

main_url = 'https://api.tdameritrade.com/v1'
td_consumer_key = f'{td_consumer_key}@AMER.OAUTHAP'

def quote(td_consumer_key, ticker):

    endpoint = f'{main_url}/marketdata/{ticker}/quotes'

    page = requests.get(url=endpoint, params={'apikey' : td_consumer_key})
    content = json.loads(page.content)
    return content

result = quote(td_consumer_key, "tsla")
print(result)
print(type(result))

#response = requests.get(url=selected_endpoint, headers=headers)
#response = requests.post(url=selected_endpoint, headers=headers, json=data)