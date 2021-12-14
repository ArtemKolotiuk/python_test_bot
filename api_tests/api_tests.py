import requests
import json

host = 'http://localhost'
port = '5000'
root_url = f"{host}:{port}"
status_201 = 201
status_200 = 200
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
payload = {'username': 'new_user', 'email': 'test@mail.com', 'password': '123'}
url = f"{root_url}/users"


def test_create_user():
    expected_body = {}
    try:
        res = requests.post(url, data=json.dumps(payload), headers=headers)
        status = res.status_code
        if status == status_201:
            try:
                body = res.json()
                if body == {}:
                    print("User were created successfully")
            except Exception:
                raise Exception(f"Exception with jsonifying content: {res.content}")
        else:
            print(f"Creation user failed - wrong response status code: {status}")
    except Exception as e:
        raise Exception(f"Request to {url} failed with exception: {e}")


def test_get_users():
    try:
        res = requests.get(url)
        status = res.status_code
        if status == status_200:
            try:
                body = res.json()
                if type(body) == list and len(body) > 0:
                    print("Users extraction successfully")
            except Exception as e:
                raise Exception(f"Failed with  {res.content}")
    except Exception as e:
        raise Exception(f"Request to {url} failed with exception: {e}")