class Vehicle:
    def __init__(self, model: str, make: str, year: int, color: str, registration_number: str, availability: bool, daily_rate: float):
        self.__model = model
        self.__make = make
        self.__year = year
        self.__color = color
        self.__registration_number = registration_number
        self.__availability = availability
        self.__daily_rate = daily_rate

    # Setters

    def set_model(self, model: str) -> None:
        self.__model = model

    def set_make(self, make: str) -> None:
        self.__make = make

    def set_year(self, year: int) -> None:
        self.__year = year

    def set_color(self, color: str) -> None:
        self.__color = color

    def set_registration_number(self, registration_number: str) -> None:
        self.__registration_number = registration_number

    def set_availability(self, availability: bool) -> None:
        self.__availability = availability

    def set_daily_rate(self, daily_rate: float) -> None:
        self.__daily_rate = daily_rate

    # Getters

    def get_model(self) -> str:
        return self.__model

    def get_make(self) -> str:
        return self.__make

    def get_year(self) -> int:
        return self.__year

    def get_color(self) -> str:
        return self.__color

    def get_registration_number(self) -> str:
        return self.__registration_number

    def get_availability(self) -> bool:
        return self.__availability

    def get_daily_rate(self) -> float:
        return self.__daily_rate
