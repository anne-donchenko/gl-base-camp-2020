import requests
from config.config import Config
from endpoints.endpoints import Endpoints
from urllib.parse import urljoin

class UsersApiClient():
   
    @staticmethod
    def _prepare_url(url, base_url=Config.BASE_URL):
        #todo: check how to prepare url properly
        # e.g. url.join(urls)
        return urljoin(base_url, url)

    @staticmethod
    def list_users():
         return requests.get(
                url=UsersApiClient._prepare_url(Endpoints.USERS)
            ).json()

    @staticmethod
    def create_user(user_details):
        return requests.post(
            url=UsersApiClient._prepare_url(Endpoints.USERS), 
            json=user_details
        ).json()

    @staticmethod
    def update_user(user_details, user_id):
        return requests.put(
            url=UsersApiClient._prepare_url(Endpoints.USERS + '/' + user_id), 
            json=user_details
        ).json()

    @staticmethod
    def delete_user(user_id):
        return requests.delete(
           url=UsersApiClient._prepare_url(Endpoints.USERS)
            )
        