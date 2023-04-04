from .data_loader.cars_loader import get_cars
from .data_loader.json_loader import get_cars_data_json
from .car.service import CarsService
from .car.car_body.model import CarBodyType
from .car.engine.model import EngineType
from .car.types import SortCriteria
from .logger.model import CustomFormatter, MyLogger

from typing import Final
from decimal import Decimal

import logging


def main() -> None:
    """LOGGING"""
    logger = MyLogger.get_logger()

    """APP"""
    logger.warning('STARTING APP')

    FILENAME: Final[str] = 'cars_app/data/cars.json'

    cars_data = get_cars_data_json(FILENAME)
    logger.info('Successfully loaded cars data')

    cars = get_cars(cars_data)

    cars_service = CarsService(cars)
    logger.info('Successfully created CarsService')

    logger.debug('Cars sorted by specified criteria')
    print(cars_service.sort_by(SortCriteria.ENGINE_POWER, reverse=True))
    print(cars_service.sort_by(SortCriteria.COMPONENTS_QUANTITY, reverse=False))
    print(cars_service.sort_by(SortCriteria.WHEEL_SIZE, reverse=False))

    logger.debug('Cars with body type and price in range 100 and 170')
    print(cars_service.get_cars_with_body_type_and_price_in_range(Decimal('100'), Decimal('170'), CarBodyType.SEDAN))

    logger.debug('Cars with specified engine type')
    print(cars_service.get_cars_with_engine_type(EngineType.DIESEL))

    logger.debug('Statistics about cars')
    print(cars_service.get_statistics())

    logger.debug('Car and mileage')
    print(cars_service.get_car_and_mileage())

    logger.debug('Wheel type and cars')
    print(cars_service.get_wheel_type_and_cars())

    logger.debug('Cars with specified components')
    print(cars_service.get_cars_with_components([
        "ABS",
        "HEATING"
    ]))

    logger.warning('ENDING APP')
