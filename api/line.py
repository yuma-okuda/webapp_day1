
import requests
import os


def send_message(notification_message):
    # LineNotify 連携用トークン・キー準備
    line_notify_token = '自分のトークン'
    line_notify_api = 'https://notify-api.line.me/api/notify'

    # httpヘッダー設定
    headers = {'Authorization': f'Bearer {line_notify_token}'}

    # トーク送信メッセージ設定
    data = {'message': f'message: {notification_message}'}

    # Post実行
    requests.post(line_notify_api, headers=headers, data=data)

def send_image():
    # LineNotify 連携用トークン・キー準備
    line_notify_token = '自分のトークン'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    path = '画像のパス'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': 'message: test'}
    files = {"imageFile":open(path,'rb')}
    requests.post(line_notify_api,headers=headers,data=data ,files=files)

if __name__ == "__main__":
    send_message()