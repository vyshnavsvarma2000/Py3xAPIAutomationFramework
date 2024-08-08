# Read the CSV or Excel file
# Create a function create_token which can take values from the excel file
# Verify the expected result


# Read the Excel - openpyxl

import openpyxl
import requests
from src.constants.api_constants import APIConstants
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import post_request


def create_auth_request(username, password):
    payload = {
        "username": username,
        "passsword": password
    }
    response = post_request(APIConstants.url_create_token(), headers=Utils().common_headers_json(), auth=None,
                            payload=payload, in_json=False)
    return response


def test_create_auth_with_excel(read_credentials_from_excel):
    filepath = "E:\The TESTING ACADEMY\API_AUTOMATION\Py3xAPIAutomationFramework\tests\tests\datadriventesting\testdata_ddt_123.xlsx"
    credentials = read_credentials_from_excel(filepath=filepath)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        response = create_auth_request(username=username, password=password)
        print(response.status_code)