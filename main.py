# ライブラリのインポート
import tweepy
import requests, json, os
from pprint import pprint
from datetime import datetime, date, timedelta

# api-keyとかの準備
## twitter
consumer_key='CONSUMER_KEY'
consumer_secret='CONSUMER_KEY_SECRET'
access_token_key='ACCESS_TOKEN_KEY'
access_token_secret='ACCESS_TOKEN_KEY_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

## ApexLegends-tracker
url = "https://public-api.tracker.gg/v2/apex/standard/profile/{PLATFORM}/{ID}"
header = {"TRN-Api-key":'TRN_API_KEY'}

res = requests.get(url, headers=header).json()

# 前回トータルキル数の読み込み
f = open(R"last_kills.txt", 'r', encoding='UTF-8')

last_kills = f.read()

f.close()

# 現在のトータルキル数の読み込み
now_kills = int(res['data']['segments'][0]['stats']['kills']['value'])

# 時刻の設定
today = datetime.today()
yesterday = today - timedelta(days=1)

# ツイート
api.update_status("ApexLegends:" + datetime.strftime(yesterday, '%Y-%m-%d') + "のキル数は{}です。現在のトータルキル数は{}です。".format(int(now_kills)-int(last_kills), now_kills))

# last_kills.txtの更新
f = open(R"last_kills.txt", 'w', encoding='UTF-8')

f.write(str(now_kills))

f.close()
