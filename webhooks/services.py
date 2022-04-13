import json
import requests


class WebhookService:

    @staticmethod
    def send_webhook(url, data):
        headers = {'Content-type': 'application/json'}
        try:
            json_data = json.loads(data)
            response = requests.post(url, data=json.dumps(json_data), headers=headers)
            return response.status_code
        except Exception as e:
            print(e)
            return e