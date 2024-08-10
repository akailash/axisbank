import requests
from typing import Dict

class AxisBankClient:
    def __init__(self, base_url: str, client_id: str, client_secret: str):
        self.base_url = base_url
        self.client_id = client_id
        self.client_secret = client_secret

    def _make_request(self, endpoint: str, data: Dict, headers: Dict) -> Dict:
        url = f"{self.base_url}{endpoint}"
        headers.update({
            "X-IBM-Client-Id": self.client_id,
            "X-IBM-Client-Secret": self.client_secret,
        })
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def _prepare_headers(self, additional_headers: Dict = None) -> Dict:
        headers = {
            "Content-Type": "application/json",
        }
        if additional_headers:
            headers.update(additional_headers)
        return headers
