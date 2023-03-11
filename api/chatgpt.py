import requests
import json

def send_prompt():
	API_KEY = '***'

	headers = {
		'***'
	}

	data = {
		'***'
	}


	response = requests.post('***', headers=headers, data=json.dumps(data))
	response_data = response.json()
	print(response_data['choices'][0]['message']['content'])


send_prompt()