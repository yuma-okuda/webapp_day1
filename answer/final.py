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
    return response_data['choices'][0]['message']['content']


def send_message(notification_message):
    # LineNotify 連携用トークン・キー準備
    line_notify_token = ''
    line_notify_api = 'https://notify-api.line.me/api/notify'

    # httpヘッダー設定
    headers = {'Authorization': f'Bearer {line_notify_token}'}

    # トーク送信メッセージ設定
    data = {'message': f'message: {notification_message}'}

    # Post実行
    requests.post(line_notify_api, headers=headers, data=data)


if __name__ == '__main__':
    text = send_prompt()
    send_message(text)
