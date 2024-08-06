#Payloads

def payload_create_booking():
    payload = {
    "firstname": "Mark",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-01-01",
        "checkout": "2024-04-01"
    },
        "additionalneeds": "Breakfast"
    }
    return payload

def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload