import requests
import json

host = 'http://localhost'
port = '5000'
root_url = f"{host}:{port}"
user_created = 201
status_ok = 200
user_created_invalid = 400
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
user_create_payload = {'username': 'new_user', 'email': 'test@mail.com', 'password': '123'}
url = f"{root_url}/users"
invalid_create_user_payload = {'email': 'invalid_test@mail.com', 'password': '1234'}


def test_create_user():
    expected_body = {}
    try:
        res = requests.post(url, data=json.dumps(user_create_payload), headers=headers)
        status = res.status_code
        if status == user_created:
            try:
                body = res.json()
                if body == {}:
                    print(f"User were created successfully. Status: {status}")
            except Exception:
                raise Exception(f"Exception with jsonifying content: {res.content}")
        else:
            print(f"Creation user failed - wrong response status code: {status}")
    except Exception as e:
        raise Exception(f"Request to {url} failed with exception: {e}")


def test_create_user_invalid_data():
    try:
        res = requests.post(url, data=json.dumps(invalid_create_user_payload), headers=headers)
        status = res.status_code
        if status == user_created_invalid:
            try:
                body = res.json()
                message = body.get("error_message")
                if message:
                    print(f"User wasn't created, cause invalid input data with status-code: {status} \n and error_message: {message}")
            except Exception as e:
                raise Exception(f"Failed with exception {e}")
        else:
            print(f"ERROR: User created with invalid data. With status-code {status}")
    except Exception as e:
        raise Exception(f"Request to {url} failed with exception: {e}")


def test_get_users():
    try:
        res = requests.get(url)
        status = res.status_code
        if status == status_ok:
            try:
                body = res.json()
                if type(body) == list:
                    print(f"Users extraction successfully. Status-code: {status}")
            except Exception as e:
                raise Exception(f"Failed with  {res.content}")
    except Exception as e:
        raise Exception(f"Request to {url} failed with exception: {e}")
