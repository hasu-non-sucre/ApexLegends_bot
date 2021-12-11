# ライブラリのインポート
import json
import os
from datetime import date, datetime, timedelta
from pprint import pprint

import requests
import tweepy

# api-keyとかの準備
# twitter
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_KEY_SECRET'
access_token_key = 'ACCESS_TOKEN_KEY'
access_token_secret = 'ACCESS_TOKEN_KEY_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

# ApexLegends-tracker
url = "https://public-api.tracker.gg/v2/apex/standard/profile/{PLATFORM}/{ID}"
header = {"TRN-Api-key": 'TRN_API_KEY'}

res = requests.get(url, headers=header).json()

# 前回トータルキル数の読み込み
with open("last_kills.txt", 'r', encoding='UTF-8') as f:
    last_kills = f.read()


# 現在のトータルキル数の読み込み
now_kills = int(res['data']['segments'][0]['stats']['kills']['value'])

# last_kills.txtの最終更新日の取得
last_kill_day = datetime.fromtimestamp(os.path.getmtime("last_kills.txt"))

# 時刻の設定
today = datetime.today()
time_delta = today - last_kill_day

# ツイート
yesterday_date = datetime.strftime(yesterday, '%Y-%m-%d')
kills_delta = (int(now_kills)-int(last_kills)).days
api.update_status(f"ApexLegends: 直近{time_delta}日間のキル数は{kills_delta}です。現在のトータルキル数は{now_kills}です。")

# last_kills.txtの更新
with open("last_kills.txt", 'w', encoding='UTF-8') as f:
    f.write(str(now_kills))
