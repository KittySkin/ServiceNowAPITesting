from ..api_wrapper import *


class UserCredentials(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class APIWrapper:
    def __init__(self, user_credentials, instance_url):
        self.user_credentials = user_credentials
        self.instance_url = instance_url

    def call_function(self, function_pointer, *args):
        return function_pointer(self.user_credentials.username, self.user_credentials.password, self.instance_url, *args)


def get_table(username, password, instance_url, table_name):
    response = requests.get(
        f"{instance_url}/api/now/table/{table_name}",
        auth=(username, password)
    )
    return response
