import pytest
from config.config import Config
from api.users_api_client import UsersApiClient
from endpoints.endpoints import Endpoints

USER_ID = ''

def test_it_checks_user_list():
    global USER_ID
    users = UsersApiClient.list_users()
    USER_ID = str(users['data'][1]['id'])
    assert (len(USER_ID) > 0)

def test_it_checks_user_created():
    user_details = {"name": "morpheus",
                    "job": "leader"
                    }
    user = UsersApiClient.create_user(user_details)
    print(user)
    assert (user['name'] == 'morpheus')

def test_it_checks_user_updated():
    user_details = {"name": "morpheus",
                    "job": "zion resident"
                    }
    print('USER_ID=' + USER_ID)
    user = UsersApiClient.update_user(user_details, USER_ID)
    print(user)
    assert (user['job'] == 'zion resident')

def test_it_checks_user_deleted():
    result = UsersApiClient.delete_user(USER_ID)
    assert (result.status_code == 204) 