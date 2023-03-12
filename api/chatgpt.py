import requests
import json


def send_chatgpt():
    API_KEY = '***'

    headers = {
        '***'
    }

    data = {
        '***'
    }

    response = requests.post('***', headers=headers, data=json.dumps(data))
    response_data = response.json()


if __name__ == '__main__':
    send_chatgpt()
