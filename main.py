import sys

import requests
import csv
from pprint import pprint
import libs.auth_lib as auth_lib


def main(argc, argv):
    instance_url = auth_lib.get_instance_url()
    username = auth_lib.get_username()
    password = auth_lib.get_password()

    response = requests.get(
        f"{instance_url}/api/now/table/incident",
        auth=(username, password)
    )

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

    pprint(response.json())

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
