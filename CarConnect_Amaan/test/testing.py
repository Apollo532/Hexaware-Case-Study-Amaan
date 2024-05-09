import unittest
from datetime import datetime
from dao.CarConnectImpl import CustomerService, VehicleService
from entity.Customers import Customer
from entity.Vehicles import Vehicle
from exceptions.customExceptions import AuthenticationException



class TestCustomerAuthentication(unittest.TestCase):

    def setUp(self):
        self.customer_service = CustomerService()

    def test_invalid_credentials(self):
        with self.assertRaises(AuthenticationException):
            self.customer_service.authenticateCustomer("invalid_username", "invalid_password")


class TestCustomerUpdate(unittest.TestCase):

    def setUp(self):
        self.customer_service = CustomerService()

    def test_update_customer_info(self):
        # Create a new customer
        new_customer = Customer("Max", "Verstappen", "maxvers@example.com", "2993883202", "Paris, FR", "versmax", "maxv", '2024-01-01')
        # Register the customer
        self.customer_service.registerCustomer(new_customer)

        # Update customer information
        updated_customer = Customer("John", "Cena", "cena@gmail.com", "9192832920", "Miami,FL", "cenajohn", "uccme", '2024-02-01')
        self.customer_service.updateCustomer(updated_customer, customer_id=1)

        # Fetch the updated customer details
        updated_customer_data = self.customer_service.getCustomerById(1)

        # Check if the customer's phone number and address are updated
        self.assertIsNotNone(updated_customer_data)
        self.assertEqual(updated_customer_data[4], "9192832920")
        self.assertEqual(updated_customer_data[5], "Miami,FL")


class TestVehicleManagement(unittest.TestCase):

    def setUp(self):
        # Initialize VehicleService for testing
        self.vehicle_service = VehicleService()

    def test_add_new_vehicle(self):
        # Create a new vehicle
        details = ("Toyota", "Fortuner", 2022, "Grey", "COV239", 1, 90.00)
        new_vehicle = Vehicle("Toyota", "Fortuner", 2022, "Grey", "COV239", 1, 90.00)
        # Add the new vehicle
        self.vehicle_service.addVehicle(new_vehicle)
        # Retrieve the latest inserted vehicle
        latest_vehicle = self.vehicle_service.getLatestInsertedVehicle()
        # Check if the latest inserted vehicle matches the new vehicle
        self.assertEqual(details[4], latest_vehicle.get_registration_number())

    def test_update_vehicle_details(self):
        # Update vehicle details
        updated_vehicle = Vehicle("Toyota", "Camry", 2022, "Black", "XYZ123", 1, 60.00)
        self.vehicle_service.updateVehicle(updated_vehicle, vehicle_id=1)
        # Fetch the updated vehicle details
        updated_vehicle_data = self.vehicle_service.getVehicleById(1)
        # Check if the vehicle's color and daily rate are updated
        self.assertEqual(updated_vehicle_data[4], "Black")
        self.assertEqual(updated_vehicle_data[7], 60.00)

    def test_get_available_vehicles(self):
        # Create a new vehicle with availability set to True
        details = ('Toyota Camry', 'Toyota', 2018, 'Black', 'ABC123', 1, 60.00)
        available_vehicle = Vehicle("Toyota Camry", "Toyota", 2018, "Black", "ABC123", 1, 60.00)

        # Retrieve the list of available vehicles
        available_vehicles = self.vehicle_service.getAvailableVehicles()

        # Check if the available vehicle is in the list
        self.assertEqual(details[4], available_vehicles[0].get_registration_number())

    def test_show_all_vehicles(self):
        vehicles = self.vehicle_service.showAllVehicles()
        self.assertIsNotNone(vehicles)


if __name__ == '__main__':
    unittest.main()