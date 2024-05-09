from datetime import date

class Customer:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str, address: str, username: str, password: str, registration_date: date):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__username = username
        self.__password = password
        self.__registration_date = registration_date

    # Setters

    def set_first_name(self, first_name: str) -> None:
        self.__first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def set_address(self, address: str) -> None:
        self.__address = address

    def set_username(self, username: str) -> None:
        self.__username = username

    def set_password(self, password: str) -> None:
        self.__password = password

    def set_registration_date(self, registration_date: date) -> None:
        self.__registration_date = registration_date

    # Getters

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_email(self) -> str:
        return self.__email

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_address(self) -> str:
        return self.__address

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_registration_date(self) -> date:
        return self.__registration_date