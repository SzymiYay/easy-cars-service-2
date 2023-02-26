from ..car.model import Car
from ..car.validator import validate_car_data

from typing import Any


def get_cars(car_data: list[dict[str, Any]]) -> list[Car]:
    return [Car.from_dict(car) for car in car_data if validate_car_data(car)]