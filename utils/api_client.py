import requests


class ApiYandex:
    def __init__(self):
        self.base_url = "https://passport.yandex.ru"
        self.headers = {'Content-Type': 'application/json'}

    def add_new_user(self, status):
        r = requests.post(url=self.base_url + '/auth/', json=status, headers=self.headers)
        return r

    def get_(self, id_):
        r = requests.get(url=f'{self.base_url}/auth/{id_}', headers=self.headers)
        return r

    def add_notnew_user(self, status):
        r = requests.post(url=self.base_url + '/auth/', json=status, headers=self.headers)
        return r


def test_66666():
    api = ApiYandex()
    r = api.get_(1)
    print(r.text)