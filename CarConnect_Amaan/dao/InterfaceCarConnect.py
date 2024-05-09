from abc import ABC, abstractmethod

class ICustomerService(ABC):

    @abstractmethod
    def showAllCustomers(self):
        pass

    @abstractmethod
    def getCustomerById(self, customer_id):
        pass


    @abstractmethod
    def getCustomerByUsername(self,username):
        pass

    @abstractmethod
    def registerCustomer(self, customer):
        pass


    @abstractmethod
    def updateCustomer(self, customer, customer_id):
        pass


    @abstractmethod
    def deleteCustomer(self, customer_id):
        pass

    @abstractmethod
    def authenticateCustomer(self, username, password):
        pass


class IVehicleService(ABC):

    @abstractmethod
    def showAllAvailableVehicles(self):
        pass

    @abstractmethod
    def showAllVehicles(self):
        pass

    @abstractmethod
    def getVehicleById(self, vehicle_id):
        pass


    @abstractmethod
    def addVehicle(self, vehicle):
        pass

    @abstractmethod
    def updateVehicle(self, vehicle, vehicle_id):
        pass

    @abstractmethod
    def removeVehicle(self, vehicle_id):
        pass

    @abstractmethod
    def revenueByVehicle(self):
        pass

class IReservationService(ABC):

    @abstractmethod
    def getReservationById(self, reservation_id):
        pass

    @abstractmethod
    def getReservationByCustomerId(self, customer_id):
        pass


    @abstractmethod
    def createReservation(self, reservation):
        pass

    @abstractmethod
    def updateReservation(self, reservation, reservation_id):
        pass

    @abstractmethod
    def cancelReservation(self, reservation_id):
        pass
        """Cancel a reservation by its ID."""

class IAdminService(ABC):

    @abstractmethod
    def showAllAdmins(self):
        pass

    @abstractmethod
    def getAdminById(self, admin_id):
        pass

    @abstractmethod
    def getAdminByUsername(self, username):
        pass

    @abstractmethod
    def registerAdmin(self,admin):
        pass

    @abstractmethod
    def updateAdmin(self, admin, admin_id):
        pass

    @abstractmethod
    def deleteAdmin(self, admin_id):
        pass

    @abstractmethod
    def authenticateAdmin(self,username, password):
        pass
