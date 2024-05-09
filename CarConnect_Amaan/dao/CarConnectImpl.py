from datetime import datetime
from entity.Customers import Customer
from entity.Vehicles import Vehicle
from entity.Reservations import Reservation
from entity.Admin import Admin
from exceptions.customExceptions import *
from dao.InterfaceCarConnect import ICustomerService, IVehicleService, IAdminService, IReservationService
from util.DBConnector import DBConnector


class CustomerService(ICustomerService):

    def showAllCustomers(self):
        conn = DBConnector.openConnection()
        cs = conn.cursor()
        try:
            cs.execute("SELECT * FROM Customers")
            print("Customer details:")
            for row in cs.fetchall():
                print(row)
        finally:
            DBConnector.closeConnection(conn, cs)

    def getCustomerById(self, customer_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""SELECT * FROM Customers WHERE CustomerID = %s""", (customer_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f"Customer with ID {customer_id} not found")
            else:
                print(row)
                return row
        except NotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")

    def getCustomerByUsername(self, username):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""
                    SELECT * FROM Customers WHERE Username LIKE %s
                       """, (username,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f"Customer with Username {username} not found")
            else:
                print(row)
        except NotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def registerCustomer(self, customer):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            # Checking valid input of data.

            if any(char.isdigit() for char in customer.get_first_name()) or any(
                    char.isdigit() for char in customer.get_last_name()):
                raise InvalidDataException('Invalid First or Last Name')

            # phone number
            if any(char.isalpha() for char in customer.get_phone_number()):
                raise InvalidDataException('Invalid Phone Number')

            # email
            if '@' not in customer.get_email():
                raise InvalidDataException('Invalid Email')

            # Insert customer data into the database
            cs.execute("""INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                       (customer.get_first_name(), customer.get_last_name(), customer.get_email(),
                        customer.get_phone_number(), customer.get_address(), customer.get_username(),
                        customer.get_password(), customer.get_registration_date()))
            conn.commit()
            print('Customer created successfully.\n')
        except InvalidDataException as e:
            conn.rollback()
            print(e)
        finally:
            DBConnector.closeConnection(conn, cs)

    def updateCustomer(self, customer, customer_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
            customer_details = cs.fetchone()

            if customer_details:
                if any(char.isalpha() for char in customer.get_phone_number()):
                    raise InvalidDataException('Invalid Phone Number')

                if '@' not in customer.get_email() or '.' not in customer.get_email():
                    raise InvalidDataException('Invalid Email')

                cs.execute("""UPDATE Customers SET Email = %s, PhoneNumber = %s, Address = %s, Username = %s, Password = %s
                        WHERE CustomerID = %s""",
                       (customer.get_email(), customer.get_phone_number(), customer.get_address(),
                        customer.get_username(), customer.get_password(), customer_id))
                conn.commit()
                print("Customer details updated")
            else:
                raise NotFoundException('Customer not found, enter valid id')
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            DBConnector.closeConnection(conn, cs)

    def deleteCustomer(self, customer_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
            customer_details = cs.fetchone()
            if customer_details:
                cs.execute("DELETE FROM Customers WHERE CustomerID = %s", (customer_id,))
                conn.commit()
                print('Removed Customer successfully')
            else:
                raise NotFoundException('Customer not found, Enter valid ID')
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            DBConnector.closeConnection(conn, cs)

    def authenticateCustomer(self, username, password):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Customers WHERE Username = %s AND Password = %s", (username, password))
            row = cs.fetchone()
            if row:
                print("Customer details verified - Customer Authenticated")
            else:
                raise AuthenticationException("Invalid username or password for customer.")
        except AuthenticationException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def run(self, choice):
        if choice == 1:
            self.showAllCustomers()
        elif choice == 2:
            customer_id = int(input('Enter Customer ID: '))
            self.getCustomerById(customer_id)
        elif choice == 3:
            username = input('Enter Customer Username: ')
            self.getCustomerByUsername(username)
        elif choice == 4:
            self.registerCustomer()
        elif choice == 5:
            self.updateCustomer()
        elif choice == 6:
            customer_id = int(input('Enter Customer ID to delete: '))
            self.deleteCustomer(customer_id)
        elif choice == 7:
            username = input('Enter username: ')
            password = input('Enter password: ')
            self.authenticateCustomer(username, password)
        else:
            print('Incorrect choice, please try again.\n')


class VehicleService(IVehicleService):

    def showAllAvailableVehicles(self):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Vehicles WHERE Availability = 1")
            print("Available Vehicles:")
            for row in cs.fetchall():
                print(row)
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def getAvailableVehicles(self):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Vehicles WHERE Availability = 1")
            available_vehicles = [Vehicle(row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in
                                  cs.fetchall()]
            return available_vehicles
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def getLatestInsertedVehicle(self):
        latest_vehicle = None
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Vehicles ORDER BY VehicleID DESC LIMIT 1")
            row = cs.fetchone()
            if row:
                # Create a Vehicle object for the latest inserted vehicle
                latest_vehicle = Vehicle(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)
        return latest_vehicle

    def showAllVehicles(self):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Vehicles")
            print("All Vehicles:")
            for row in cs.fetchall():
                print(row)
            return cs.fetchall()
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def getVehicleById(self, vehicle_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Vehicles WHERE VehicleID = %s", (vehicle_id,))
            row = cs.fetchone()
            if row is None:
                raise VehicleNotFoundException(vehicle_id)
            else:
                print(row)
                return row
        except VehicleNotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def addVehicle(self, vehicle):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""INSERT INTO Vehicles (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
                           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                       (vehicle.get_model(), vehicle.get_make(), vehicle.get_year(),
                        vehicle.get_color(), vehicle.get_registration_number(), vehicle.get_availability(),
                        vehicle.get_daily_rate()))
            conn.commit()
            print('Vehicle added successfully.')
        except Exception as e:
            conn.rollback()
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def updateVehicle(self, vehicle, vehicle_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()

            cs.execute("SELECT * FROM Vehicles WHERE VehicleID = %s", (vehicle_id,))
            row = cs.fetchone()
            if row:
                cs.execute("UPDATE Vehicles SET Availability = %s , DailyRate = %s  WHERE VehicleID = %s",
                    (vehicle.get_availability(), vehicle.get_daily_rate(), vehicle_id))
                conn.commit()
                print("Vehicle details updated.")
            else:
                raise VehicleNotFoundException(vehicle_id)
        except Exception as e:
            conn.rollback()
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def removeVehicle(self, vehicle_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Vehicles WHERE VehicleID = %s", (vehicle_id,))
            row = cs.fetchone()
            if row:
                cs.execute("DELETE FROM Vehicles WHERE VehicleID = %s", (vehicle_id,))
                conn.commit()
                print('Vehicle removed successfully.')
            else:
                raise VehicleNotFoundException(vehicle_id)
        except Exception as e:
            conn.rollback()
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def revenueByVehicle(self):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""
                        SELECT V.VehicleID, V.Model, COALESCE(SUM(R.TotalCost), 0) AS TotalRevenue 
                        FROM Vehicles AS V
                        LEFT JOIN Reservations AS R ON V.VehicleID = R.VehicleID 
                        GROUP BY V.VehicleID, V.Model
                        """)
            print("Vehicle ID | Vehicle Name | Total Revenue")
            print("-------------------------------------------")
            for row in cs.fetchall():
                vehicle_id, vehicle_name, total_revenue = row
                print(f"{vehicle_id} | {vehicle_name} | {total_revenue}")
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def run(self, choice):
        if choice == 1:
            self.showAllAvailableVehicles()
        elif choice == 2:
            vehicle_id = int(input('Enter Vehicle ID: '))
            self.getVehicleById(vehicle_id)
        elif choice == 3:
            self.showAllVehicles()
        elif choice == 4:
            self.addVehicle()
        elif choice == 5:
            self.updateVehicle()
        elif choice == 6:
            vehicle_id = int(input('Enter Vehicle ID to remove: '))
            self.removeVehicle(vehicle_id)
        elif choice == 7:
            self.revenueByVehicle()
        else:
            print('Incorrect choice, please try again.\n')


class ReservationService(IReservationService):

    def getReservationByCustomerId(self, customer_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Reservations WHERE CustomerID = %s", (customer_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f'Reservation with Customer ID {customer_id} Not found')
            else:
                print("Reservation details:")
                print(row)
        except NotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def getReservationById(self, reservation_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Reservations WHERE ReservationID = %s", (reservation_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f'Reservation with ID {reservation_id} Not found')
            else:
                print("Reservation details:")
                print(row)
        except NotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def createReservation(self, reservation):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()

            # Check if the vehicle is available
            cs.execute('SELECT Availability FROM Vehicles WHERE VehicleID = %s', (reservation.get_vehicle_id(),))
            availability = cs.fetchone()[0]
            if availability == 0:
                raise ReservationException("Vehicle is not available for reservation.")

            # Calculate total cost
            cs.execute('SELECT DailyRate FROM Vehicles WHERE VehicleID = %s', (reservation.get_vehicle_id(),))
            rate = cs.fetchone()[0]
            difference = reservation.get_end_date() - reservation.get_start_date()
            day_diff = difference.days
            total_cost = day_diff * rate

            # Add reservation to the database
            cs.execute("""INSERT INTO Reservations (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                        VALUES (%s, %s, %s, %s, %s, %s)""",
                        (reservation.get_customer_id(), reservation.get_vehicle_id(),
                         reservation.get_start_date(), reservation.get_end_date(), total_cost, reservation.get_status()))
            conn.commit()
            print('Reservation added successfully.')
        except ReservationException as e:
            conn.rollback()
            print(f"Error occurred: {e}")
        except Exception as e:
            conn.rollback()
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def updateReservation(self, reservation, reservation_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Reservations WHERE ReservationID = %s", (reservation_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f'Reservation with ID {reservation_id} Not found')
            else:
                cs.execute('SELECT DailyRate FROM Vehicles WHERE VehicleID = (SELECT VehicleID FROM Reservations WHERE'
                             ' ReservationID = %s)', (reservation_id,))
                rate = cs.fetchone()[0]
                difference = reservation.get_end_date() - reservation.get_start_date()
                day_diff = difference.days
                total_cost = day_diff * rate
                cs.execute("""UPDATE Reservations 
                          SET StartDate = %s, EndDate = %s, TotalCost = %s
                          WHERE ReservationID = %s""",
                       (reservation.get_start_date(), reservation.get_end_date(), total_cost, reservation_id))
                conn.commit()
                print("Reservation details updated.")
        except Exception as e:
            conn.rollback()
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def cancelReservation(self, reservation_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Reservations WHERE ReservationID = %s", (reservation_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f'Reservation with ID {reservation_id} Not found')
            else:
                cs.execute("DELETE FROM Reservations WHERE ReservationID = %s", (reservation_id,))
                conn.commit()
                print('Reservation canceled successfully.')
        except Exception as e:
            conn.rollback()
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def run(self, choice):
        if choice == 1:
            customer_id = int(input('Enter Customer ID: '))
            self.getReservationByCustomerId(customer_id)
        elif choice == 2:
            reservation_id = int(input('Enter Reservation ID: '))
            self.getReservationById(reservation_id)
        elif choice == 3:
            self.createReservation()
        elif choice == 4:
            self.updateReservation()
        elif choice == 5:
            reservation_id = int(input('Enter Reservation ID to cancel: '))
            self.cancelReservation(reservation_id)
        else:
            print('Incorrect choice, please try again.\n')


class AdminService(IAdminService):

    def showAllAdmins(self):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Admin")
            print("Admin details:")
            for row in cs.fetchall():
                print(row)
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def getAdminById(self, admin_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""
                        SELECT * FROM Admin WHERE AdminID = %s
                    """, (admin_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f"Admin with ID {admin_id} not found")
            else:
                print(row)
        except NotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")

    def getAdminByUsername(self, username):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""
                    SELECT * FROM Admin WHERE Username LIKE %s
                       """, (username,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f"Admin with Username {username} not found")
            else:
                print(row)
        except NotFoundException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def registerAdmin(self, admin):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            if any(char.isdigit() for char in admin.get_first_name()) or any(
                    char.isdigit() for char in admin.get_last_name()):
                raise InvalidDataException('Invalid First or Last Name')

            # phone number
            if any(char.isalpha() for char in admin.get_phone_number()):
                raise InvalidDataException('Invalid Phone Number')

            # email
            if '@' not in admin.get_email() or '.' not in admin.get_email():
                raise InvalidDataException('Invalid Email')

            # Insert customer data into the database
            cs.execute("""INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role,
                            JoinDate)
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                       (admin.get_first_name(), admin.get_last_name(), admin.get_email(),
                        admin.get_phone_number(), admin.get_username(), admin.get_password(), admin.get_role(),
                        admin.get_join_date()))
            conn.commit()
            print('Admin Registered Successfully.\n')
        except InvalidDataException as e:
            conn.rollback()
            print(e)
        finally:
            DBConnector.closeConnection(conn, cs)

    def updateAdmin(self, admin, admin_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()

            cs.execute("""SELECT * FROM Admin WHERE AdminID = %s""", (admin_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f"Admin with ID {admin_id} not found")
            else:
                # phone number
                if any(char.isalpha() for char in admin.get_phone_number()):
                    raise InvalidDataException('Invalid Phone Number')

                # email
                if '@' not in admin.get_email() or '.' not in admin.get_email():
                    raise InvalidDataException('Invalid Email')

                cs.execute("SELECT * FROM Admin WHERE AdminID = %s", (admin_id,))
                admin_details = cs.fetchone()
                if admin_details:
                    cs.execute("""UPDATE Admin SET Email = %s, PhoneNumber = %s, Username = %s, Password = %s, Role = %s
                                WHERE AdminID = %s""",
                            (admin.get_email(), admin.get_phone_number(), admin.get_username(),
                                admin.get_password(), admin.get_role(), admin_id))
                    conn.commit()
                    print("Admin details updated")
                else:
                    print("Admin not found")
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            DBConnector.closeConnection(conn, cs)

    def deleteAdmin(self, admin_id):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("""SELECT * FROM Admin WHERE AdminID = %s""", (admin_id,))
            row = cs.fetchone()
            if row is None:
                raise NotFoundException(f"Admin with ID {admin_id} not found")
            else:
                cs.execute("DELETE FROM Admin WHERE AdminID = %s", (admin_id,))
                conn.commit()
                print('Removed Admin successfully')
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            DBConnector.closeConnection(conn, cs)

    def authenticateAdmin(self, username, password):
        try:
            conn = DBConnector.openConnection()
            cs = conn.cursor()
            cs.execute("SELECT * FROM Admin WHERE Username = %s AND Password = %s", (username, password))
            row = cs.fetchone()
            if row:
                print('Admin details verified. Admin authenticated')
            else:
                raise AuthenticationException("Invalid username or password for admin.")
        except AuthenticationException as e:
            raise e
        except Exception as e:
            print(f"Error occurred: {e}")
        finally:
            DBConnector.closeConnection(conn, cs)

    def run(self, choice):
        if choice == 1:
            self.showAllAdmins()
        elif choice == 2:
            admin_id = int(input('Enter Admin ID: '))
            self.getAdminById(admin_id)
        elif choice == 3:
            username = input('Enter Admin Username: ')
            self.getAdminByUsername(username)
        elif choice == 4:
            self.registerAdmin()
        elif choice == 5:
            self.updateAdmin()
        elif choice == 6:
            admin_id = int(input('Enter Admin ID to delete: '))
            self.deleteAdmin(admin_id)
        elif choice == 7:
            username = input('Enter username: ')
            password = input('Enter password: ')
            self.authenticateAdmin(username, password)
        else:
            print('Incorrect choice, please try again.\n')
