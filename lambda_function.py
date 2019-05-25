
# coding:utf-8

import requests
import json
import random
from env import l,url,SLACK_URL

def lambda_handler(event, context):
    get = getStore(l,url)
    send_slack(get,SLACK_URL)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getStore(l,url):
    res = requests.get(url)
    lists = json.loads(res.text)
    if list:
        text = lists[random.choice(l)]['name']
        return text

def send_slack(getStore,SLACK_URL):
    content = getStore
    
    payload = {
        'username': 'lunch time',
        "text": content,
        "icon_emoji": ':sushi:',
    }

    data = json.dumps(payload)

    requests.post(SLACK_URL, data)
    
