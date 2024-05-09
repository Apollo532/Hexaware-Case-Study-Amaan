from datetime import date

class Admin:
    def __init__(self,  first_name: str, last_name: str, email: str, phone_number: str, username: str, password: str, role: str, join_date: date):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__username = username
        self.__password = password
        self.__role = role
        self.__join_date = join_date

    # setters

    def set_first_name(self, first_name: str) -> None:
        self.__first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self.__last_name = last_name

    def set_email(self, email: str) -> None:
        self.__email = email

    def set_phone_number(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def set_username(self, username: str) -> None:
        self.__username = username

    def set_password(self, password: str) -> None:
        self.__password = password

    def set_role(self, role: str) -> None:
        self.__role = role

    def set_join_date(self, join_date: date) -> None:
        self.__join_date = join_date

    # getters

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_email(self) -> str:
        return self.__email

    def get_phone_number(self) -> str:
        return self.__phone_number

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_role(self) -> str:
        return self.__role

    def get_join_date(self) -> date:
        return self.__join_date