import requests
import json


def send_prompt():
    API_KEY = ''

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_KEY
    }

    data = {
        'model': 'gpt-3.5-turbo',
        "messages": [{"role": "user", "content": "WBCについて説明して"}]

    }

    response = requests.post(
        'https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))
    response_data = response.json()
    print(response_data['choices'][0]['message']['content'])


send_prompt()
