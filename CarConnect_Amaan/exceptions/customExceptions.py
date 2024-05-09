class VehicleNotFoundException(Exception):
    def __init__(self, vehicle_id):
        super().__init__(f"Vehicle with ID {vehicle_id} not found in the database.")
        self.vehicle_id = vehicle_id


class AuthenticationException(Exception):
    def __init__(self, message = "Cannot Verify Details"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ReservationException(Exception):
    def __init__(self, message = "Invalid reservation"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

class NotFoundException(Exception):
    def __init__(self, message = "Not found in database"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class InvalidDataException(Exception):
    def __init__(self, message="Invalid Data"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message