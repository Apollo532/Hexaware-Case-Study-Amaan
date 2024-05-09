from dao.CarConnectImpl import CustomerService , VehicleService, ReservationService, AdminService
from entity.Customers import Customer
from entity.Vehicles import Vehicle
from entity.Reservations import Reservation
from entity.Admin import Admin
from entity.Admin import Admin
from datetime import datetime
from exceptions.customExceptions import *
from util.DBConnector import DBConnector


def main():
    while True:
        print("\nMain Menu")
        print("---------")
        print("1. Manage Customers")
        print("2. Manage Vehicles")
        print("3. Manage Reservations")
        print("4. Manage Admins")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            manage_customers()
        elif choice == 2:
            manage_vehicles()
        elif choice == 3:
            manage_reservations()
        elif choice == 4:
            manage_admins()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")


def manage_customers():

    customer_service = CustomerService()
    while True:
        print("\nCustomer Management")
        print("-----------------")
        print("1. Show all customers")
        print("2. Get customer by ID")
        print("3. Get customer by username")
        print("4. Register new customer")
        print("5. Update customer details")
        print("6. Delete customer")
        print("7. Authenticate Customer")
        print("8. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        if choice == 8:
            break
        elif choice == 4:
            # Register new customer
            first_name = input("Enter customer's first name: ")
            last_name = input("Enter customer's last name: ")
            email = input("Enter customer's email: ")
            phone = input("Enter customer's phone number: ")
            address = input("Enter customer's address: ")
            username = input("Enter customer's username: ")
            password = input("Enter customer's password: ")
            reg_date = input("Enter customer's registration date YYYY-MM-DD: ")
            register_date = datetime.strptime(reg_date, '%Y-%m-%d')
            new_customer = Customer(first_name, last_name, email,
                                    phone, address, username, password, register_date)
            try:
                customer_service.registerCustomer(new_customer)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == 5:
            #Update
            customer_id = int(input('Enter Customer_id: '))
            email = input("Enter customer's new email: ")
            phone = input("Enter customer's new phone number: ")
            address = input("Enter customer's new address: ")
            username = input("Enter customer's new username: ")
            password = input("Enter customer's new password: ")
            customer = Customer('', '', email,
                                    phone, address, username, password, '')
            try:
                customer_service.updateCustomer(customer,customer_id)
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                customer_service.run(choice)
            except Exception as e:
                print(f"Error: {e}")


def manage_vehicles():
    vehicle_service = VehicleService()
    while True:
        print("\nVehicle Management")
        print("-----------------")
        print("1. Show all available vehicles")
        print("2. Get vehicle by ID")
        print("3. Show all vehicles")
        print("4. Add new vehicle")
        print("5. Update vehicle details")
        print("6. Remove vehicle")
        print("7. Show revenue by vehicle")
        print("8. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        if choice == 8:
            break
        elif choice == 4:
            # Add new vehicle
            model = input("Enter vehicle's model: ")
            make = input("Enter vehicle's make: ")
            year = int(input("Enter vehicle's year: "))
            color = input("Enter vehicle's color: ")
            reg_number = input("Enter vehicle's registration number: ")
            availability = int(input("Enter vehicle's availability (0 for unavailable, 1 for available): "))
            daily_rate = float(input("Enter vehicle's daily rate: "))
            new_vehicle = Vehicle(model, make, year, color, reg_number, availability, daily_rate)
            try:
                vehicle_service.addVehicle(new_vehicle)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == 5:
            vehicle_id = int(input('Enter vehicle id: '))
            availability = int(input("Enter vehicle's new availability (0 for unavailable, 1 for available): "))
            daily_rate = float(input("Enter vehicle's new  daily rate: "))
            vehicle = Vehicle('','','','','', availability, daily_rate)
            try:
                vehicle_service.updateVehicle(vehicle, vehicle_id)
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                vehicle_service.run(choice)
            except Exception as e:
                print(f"Error: {e}")


def manage_reservations():
    reservation_service = ReservationService()
    while True:
        print("\nReservation Management")
        print("---------------------")
        print("1. Get reservation by customer ID")
        print("2. Get reservation by reservation ID")
        print("3. Create new reservation")
        print("4. Update reservation details")
        print("5. Cancel reservation")
        print("6. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        if choice == 6:
            break
        elif choice == 3:
            # Create new reservation
            customer_id = int(input("Enter customer ID: "))
            vehicle_id = int(input("Enter vehicle ID: "))
            s_date = input("Enter start date (YYYY-MM-DD): ")
            e_date = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(s_date, '%Y-%m-%d')
            end_date = datetime.strptime(e_date, '%Y-%m-%d')
            status = input("Enter status (e.g., Confirmed, Completed, Pending): ")
            new_reservation = Reservation(customer_id, vehicle_id, start_date, end_date, '',status)
            try:
                reservation_service.createReservation(new_reservation)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == 4:
            # Create new reservation
            reservation_id = int(input('Enter reservation id to update details: '))
            s_date = input("Enter start date (YYYY-MM-DD): ")
            e_date = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(s_date, '%Y-%m-%d')
            end_date = datetime.strptime(e_date, '%Y-%m-%d')
            status = input("Enter status (e.g., Pending, Confirmed, Completed): ")
            reservation = Reservation('', '', start_date, end_date,'', status)
            try:
                reservation_service.updateReservation(reservation, reservation_id)
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                reservation_service.run(choice)
            except Exception as e:
                print(f"Error: {e}")


def manage_admins():
    admin_service = AdminService()
    while True:
        print("\nAdmin Management")
        print("----------------")
        print("1. Show all admins")
        print("2. Get admin by ID")
        print("3. Get admin by username")
        print("4. Register new admin")
        print("5. Update admin details")
        print("6. Delete admin")
        print("7. Authenticate Admin")
        print("8. Back to Main Menu")

        choice = int(input("Enter your choice: "))
        if choice == 8:
            break
        elif choice == 4:
            # Register new admin
            first_name = input("Enter admin first name: ")
            last_name = input("Enter admin last name: ")
            email = input("Enter admin email: ")
            phone = input("Enter admin phone number: ")
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            role = input("Enter admin role: ")
            j_date = input("Enter admin join date (YYYY-MM-DD): ")
            join_date = datetime.strptime(j_date, '%Y-%m-%d')
            new_admin = Admin(first_name, last_name, email, phone, username, password, role, join_date)
            try:
                admin_service.registerAdmin(new_admin)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == 5:
            admin_id = int(input('Enter admin id to update: '))
            email = input("Enter new admin email: ")
            phone = input("Enter new admin phone number: ")
            username = input("Enter new admin username: ")
            password = input("Enter new  admin password: ")
            role = input("Enter admin new  role: ")
            admin = Admin('', '', email, phone, username, password, role, '')
            try:
                admin_service.updateAdmin(admin, admin_id)
            except Exception as e:
                print(f"Error: {e}")
        else:
            try:
                admin_service.run(choice)
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
