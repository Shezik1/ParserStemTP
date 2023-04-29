from steampy.client import Asset
from steampy.client import SteamClient
from steampy.utils import GameOptions, get_key_value_from_url, account_id_to_steam_id
import requests
import json
from colorama import init, Fore
from colorama import Back
from colorama import Style

import pickle
import os

login = 'login'
password = 'password'
api_key = 'apikey'


def log_on_steam():
    global steam_client
    if os.path.isfile(f'C:/Users/Admin/Desktop/{login}.pkl'):  # Project Path
        print("Using previous session")
        with open(f'C:/Users/Admin/Desktop/{login}.pkl', 'rb') as f:  # Project Path
            steam_client = pickle.load(f)
    else:
        print("You not authorized, trying to login into Steam")
        print("Signing in steam account")
        steam_client = SteamClient(api_key)
        steam_client.login(login, password, f"C:/Users/Admin/Desktop/Kal/{login}.json")  # Path to json file
        print("Saving session")
        with open(f'C:/Users/Admin/Desktop/{login}.pkl', 'wb') as f:  # Project Path
            pickle.dump(steam_client, f)
    print("Success")


log_on_steam()
her = steam_client.her()
item_buy = her[0]
item_sold = her[1]
all_item = []
i = 0
while i != len(item_buy):
    if item_buy[i].split("@")[1] not in all_item:
        all_item.append(item_buy[i].split("@")[1])
    i += 1
i = 0
while i != len(item_sold):
    if item_sold[i].split("@")[1] not in all_item:
        all_item.append(item_sold[i].split("@")[1])
    i += 1

price_buy = []
how_buy = []
i = 0
while i != len(all_item):
    price2 = 0
    how_buy2 = 0
    i2 = 0
    while i2 != len(item_buy):
        if all_item[i] in item_buy[i2]:
            price2 += float(item_buy[i2].split()[-1])
            how_buy2 += 1
        i2 += 1
    how_buy.append(how_buy2)
    price_buy.append(price2)
    i += 1

price_sold = []
how_sold = []
i = 0
while i != len(all_item):
    price2 = 0
    how_sold2 = 0
    i2 = 0
    while i2 != len(item_sold):
        if all_item[i] in item_sold[i2]:
            price2 += float(item_sold[i2].split()[-1])
            how_sold2 += 1
        i2 += 1
    how_sold.append(how_sold2)
    price_sold.append(price2)
    i += 1
i = 0
while i != len(all_item):
    print()
    if how_buy[i] != 0:
        print(f"{Fore.RED}Было потрачено на покупке {how_buy[i]} айтемов ({all_item[i]}) {price_buy[i]} средняя цена покупки {price_buy[i]/how_buy[i]}")
    if how_sold[i] != 0:
        print(f"{Fore.GREEN}Было получено на продаже {how_sold[i]} айтемов ({all_item[i]}) {price_sold[i]} средняя цена продажи {price_sold[i]/how_sold[i]}")
    i += 1
