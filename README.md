# Python API Automation Framework

Hybrid Custom Framework to Test the REST APIs

![Screenshot 2023-12-08 at 8 20 27 AM](https://github.com/PramodDutta/Py1xAPIAutomation/assets/1409610/a09647ad-720b-4afb-8d33-b69e4710cee4)



## Tech Stack
1. Python 3.11
2. Requests - HTTP Requests
3. PyTest - Testing Framework
4. Reporting - Allure Report, PyTest HTML
5. Test Data - CSV, Excel, JSON
6. Parallel Execution - x distribute



## How to Install Packages
`` pip install requests pytest pytest-html faker allure-pytest jsonschema
``

## To Freeze your Package version
`` pip freeze > requirements.txt ``

## To Install te Freeze Version
``pip install -r requirements.txt``


## How to run your Testcase Parallel 
`` pip install pytest-xdist ``


``pytest -n auto tests/integration_test/test_create_booking.py -s -v
``

## To Work with the Excel
``pip install openpyxl``


## To work wit JSON Schema
```pip install jsonschema```





# How to run via Jenkins(CI/CD)

  ![Screenshot 2024-04-08 at 7 55 21 AM](https://github.com/PramodDutta/Py2xAPIAutomationFramework/assets/1409610/f6901407-910b-4ea2-a329-0a4433f7e240)

- Jenkins Run Process
- Install the Jenkins - jenkins dowload
- Install the JDK  (open JDK)
- https://jdk.java.net/21/
- Set it into the Global Config - http://localhost:8080/manage/configureTools/
- Install the Plugins - http://localhost:8080/manage/pluginManager/
  - Allure
- HTML Report
- GITHUB - Repo - https://github.com/PramodDutta/Py2xAPIAutomationFramework.git

 