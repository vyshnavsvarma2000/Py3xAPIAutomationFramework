import pytest
import allure

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that create booking and bookingid shouldn't be null")
    @allure.description("Create a booking from the payload and verify that bookingid should not be null")
    def test_create_booking_positive(self):
        pass