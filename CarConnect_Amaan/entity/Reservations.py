from datetime import date

class Reservation:
    def __init__(self, customer_id: int, vehicle_id: int, start_date: date, end_date: date, total_cost: float, status: str):
        self.__customer_id = customer_id
        self.__vehicle_id = vehicle_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__total_cost = total_cost
        self.__status = status

    # Setters

    def set_customer_id(self, customer_id: int) -> None:
        self.__customer_id = customer_id

    def set_vehicle_id(self, vehicle_id: int) -> None:
        self.__vehicle_id = vehicle_id

    def set_start_date(self, start_date: date) -> None:
        self.__start_date = start_date

    def set_end_date(self, end_date: date) -> None:
        self.__end_date = end_date

    def set_total_cost(self, total_cost: float) -> None:
        self.__total_cost = total_cost

    def set_status(self, status: str) -> None:
        self.__status = status

    # Getters


    def get_customer_id(self) -> int:
        return self.__customer_id

    def get_vehicle_id(self) -> int:
        return self.__vehicle_id

    def get_start_date(self) -> date:
        return self.__start_date

    def get_end_date(self) -> date:
        return self.__end_date

    def get_total_cost(self) -> float:
        return self.__total_cost

    def get_status(self) -> str:
        return self.__status