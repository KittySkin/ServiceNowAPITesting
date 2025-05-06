import csv
from pprint import pprint
import sys

from libs.api_wrapper import api_wrapper
import libs.auth_lib as auth_lib


def main(argc, *argv):
    instance_url = auth_lib.get_instance_url()
    username = auth_lib.get_username()
    password = auth_lib.get_password()

    # In this example we have 2 possible ways to do API calls. First approach is through the usage of a wrapper class.
    # We create the APIWrapper object instance passing it the UserCredentials object and the instance url.
    # Then we use the call_function functionality to query calls without the need to pass the user, password and url.
    user_credentials = api_wrapper.UserCredentials(username, password)
    api_wrapper_object = api_wrapper.APIWrapper(user_credentials, instance_url)
    response_using_class = api_wrapper_object.call_function(api_wrapper.get_table, 'incident', category='hardware')

    # The other approach is using the regular function that requires the user, password and url to be passed at every
    # call, but do not require the creation of an APIWrapper instance, neither a UserCredentials object.
    # response_stand_alone = api_wrapper.get_table(username, password, instance_url, 'incident')

    # The below section turns the incidents into a csv file, used as an example only, should be abstracted into its own
    # functionality down the road.

    # csv_file = open("./incidents.csv", "w")
    # csv_writer = csv.writer(csv_file)
    # c = 0
    #
    # for emp in response.json()['result']:
    #     if c == 0:
    #         # Writing headers of CSV file
    #         h = emp.keys()
    #         csv_writer.writerow(h)
    #         c += 1
    #
    #     # Writing data of CSV file
    #     csv_writer.writerow(emp.values())
    #
    # csv_file.close()

    # Sample handling status code before attempting to manipulate the response:
    if response_using_class.status_code == 200:
        pprint(response_using_class.json())

    # if response_stand_alone.status_code == 200:
    #    pprint(response_stand_alone.json())


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
