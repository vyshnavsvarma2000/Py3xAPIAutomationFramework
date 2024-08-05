# API-Constants - Class which contain all the endpoints
# Keep the URL's

class APIConstants(object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    #PUT, PATCH, DELETE -> bookingid

    def url_patch_put_delete(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
