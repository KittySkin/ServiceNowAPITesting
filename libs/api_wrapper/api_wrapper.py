from ..api_wrapper import *


class UserCredentials(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class APIWrapper:
    """
    APIWrapper class, the goal of this class is to handle calls to the REST API without needing to pass user credentials
    and instance url over and over without hard linking the functions to the class itself to provide a versatile approach
    to API calls.
    """
    def __init__(self, user_credentials, instance_url):
        self.user_credentials = user_credentials
        self.instance_url = instance_url

    def call(self, function_pointer, *args, **kwargs):
        """
        Calls the function passing the user credentials and url automatically.
        :param function_pointer: Function to be called.
        :param args: Comma separated arguments to be passed to the function.
        :param kwargs: Arguments to be passed using keyword arguments.
        :return: Output of the function call.
        """
        return function_pointer(self.user_credentials.username, self.user_credentials.password, self.instance_url,
                                *args, **kwargs)


def get_table(username, password, instance_url, table_name, sys_id=None, category=None):
    endpoint_url = f"{instance_url}/api/now/table/{table_name}"
    # Construct the query string and URL encode it
    if sys_id:
        endpoint_url += f'/{sys_id}'

    if category:
        endpoint_url += f"?sysparm_query=category%3D{category}"

    response = requests.get(
        url=endpoint_url,
        auth=(username, password),
        headers={"Content-Type": "application/json", "Accept": "application/json"}
    )
    return response

def delete_table(username, password, instance_url, table_name, sys_id):
    response = requests.delete(
        f"{instance_url}/api/now/table/{table_name}/{sys_id}",
        auth=(username, password)
    )
    return response

def patch_table(username, password, instance_url, table_name, sys_id, update_data):
    response = requests.patch(
        f"{instance_url}/api/now/table/{table_name}/{sys_id}",
        auth=(username, password),
        data=update_data
    )
    return response

def post_table(username, password, instance_url, table_name, update_data):
    response = requests.post(
        f"{instance_url}/api/now/table/{table_name}",
        auth=(username, password),
        data=update_data
    )
    return response

def put_table(username, password, instance_url, table_name, update_data):
    response = requests.put(
        f"{instance_url}/api/now/table/{table_name}",
        auth=(username, password),
        data=update_data
    )
    return response
