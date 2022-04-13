import json
import requests


class WebhookService:

    @staticmethod
    def send_webhook(url, data):
        headers = {'Content-type': 'application/json'}
        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            return response.status_code
        except Exception as e:
            print(e)
            return e