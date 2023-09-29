import requests
from typing import Any


class ApiClient:
    def __init__(self):
        self.base_url = ''
        self.cookies = ''
        self.latest_request = None

    def get(self, path: str, headers: str = None, params: dict[str, Any] = None, time_out: int = 180):
        self.latest_request = requests.get(url=f'{self.base_url}{path}', headers=headers, params=params, timeout=time_out)
        self.check_status_code(status_code = 200)

    def check_status_code(self, status_code: int):
        assert status_code == self.latest_request.status_code, f'Не правильный статус код ожидади {status_code}, получили {self.latest_request.status_code}'

    def post(self, path: str, headers: str = None, params:dict[str, Any] = None, time_out: int = 180, data=None, json=None):
        self.latest_request = requests.post(url=f'{self.base_url}{path}', headers=headers, params=params, timeout=time_out, data = data, json = json)
        self.check_status_code(status_code=200)



