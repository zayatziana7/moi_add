import requests
import pytest




class ApiPet:
    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"
        self.headers = {'Content-Type': 'application/json'}

    def add_new_pet(self, id_pet: int, name_pet: str, status: str):
        data = {
            "id": id_pet,
            "category": {
                "id": 0,
                "name": ''
            },
            "name": name_pet,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": status
        }
        r = requests.post(url=self.base_url + '/pet', json=data, headers=self.headers)
        return r

    def delete_pet(self, id_pet: int):
        r = requests.delete(url=f'{self.base_url}/pet/{id_pet}', headers=self.headers)
        return r

    def put_pet(self, id_pet: int, name_pet: str, status: str):
        data = {
            "id": id_pet,
            "category": {
                "id": 0,
                "name": ''
            },
            "name": name_pet,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": status
        }
        r = requests.post(url=self.base_url + '/pet', json=data, headers=self.headers)
        return r

    def get_pet(self, id_pet: int):
        r = requests.get(url=f'{self.base_url}/pet/{id_pet}', headers=self.headers)
        return r


@pytest.mark.parametrize('id_pet, name, status',
                         [[123, 'DFGH', 'available'], [34543, 'Iana', 'pending'], [111, 'Olo', 'sold']])
def test_add(id_pet, name, status):
    api = ApiPet()
    r = api.add_new_pet(id_pet, name, status)
    assert r.status_code == 200
    r = api.delete_pet(id_pet)
    assert r.status_code == 200


@pytest.mark.parametrize('id_pet, name, status',
                         [[1111, 'DFGH', 'available'], [2222, 'Iana', 'pending'], [3333, 'Olo', 'sold']])
def test_put_add(id_pet, name, status):
    api = ApiPet()
    r = api.put_pet(id_pet, name, status)
    assert r.status_code == 200
    print(r.json())


def test_get_pets():
    api = ApiPet()
    r = api.get_pet(1111)
    print(r.json())
    assert r.status_code ==200


def test_uu():
    num_list = [1, 2, 3, 4, 5]
    for i in num_list:
        print(i)
    itr = iter(num_list)
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))

class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration

s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)


