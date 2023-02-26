from cars_app.data_loader.cars_loader import get_cars
from cars_app.car.model import Car
from cars_app.car.service import CarsService
from cars_app.car.engine.model import Engine, EngineType
from cars_app.car.car_body.model import CarBody, CarBodyColor, CarBodyType
from cars_app.car.wheel.model import Wheel, TyreType

from decimal import Decimal

import pytest
import unittest

class TestCarsLoader(unittest.TestCase):

    def setUp(self) -> None:
        self.cars = [
            {
                "model": "AUDI",
                "price": 120,
                "mileage": 12000,
                "engine": {
                    "type": "DIESEL",
                    "power": 210.0
                },
                "carBody": {
                    "color": "BLACK",
                    "type": "HATCHBACK",
                    "components": [
                        "ABS",
                        "AIR CONDITIONING"
                    ]
                },
                "wheel": {
                    "type": "SUMMER",
                    "model": "PIRELLI",
                    "size": 18
            }
        },
        {
            "model": "BMW",
            "price": 160,
            "mileage": 25000,
            "engine": {
                "type": "LPG",
                "power": 250.0
            },
            "carBody": {
                "color": "GREEN",
                "type": "SEDAN",
                "components": [
                    "ABS",
                    "HEATING"
                ]
            },
            "wheel": {
                "type": "WINTER",
                "model": "X6",
                "size": 21
            }
        },
        {
            "model": "VOLVO",
            "price": 100,
            "mileage": 5000,
            "engine": {
                "type": "GASOLINE",
                "power": 1300.0
            },
            "carBody": {
                "color": "BLUE",
                "type": "COMBI",
                "components": [
                    "ABS",
                    "HEATING",
                    "GPS"
                ]
            },
            "wheel": {
                "type": "SUMMER",
                "model": "MEGHAN",
                "size": 19
            }
        }
    ]

    def test_get_cars(self):
        expected_result = [
            Car(model='AUDI', price=Decimal('120'), mileage=12000, engine=Engine(type=EngineType.DIESEL, power=210.0),
                carBody=CarBody(color=CarBodyColor.BLACK, type=CarBodyType.HATCHBACK,
                                components=['ABS', 'AIR CONDITIONING']),
                wheel=Wheel(model='PIRELLI', size=18, type=TyreType.SUMMER)),
            Car(model='BMW', price=Decimal('160'), mileage=25000, engine=Engine(type=EngineType.LPG, power=250.0),
                carBody=CarBody(color=CarBodyColor.GREEN, type=CarBodyType.SEDAN, components=['ABS', 'HEATING']),
                wheel=Wheel(model='X6', size=21, type=TyreType.WINTER)),
            Car(model='VOLVO', price=Decimal('100'), mileage=5000,
                engine=Engine(type=EngineType.GASOLINE, power=1300.0),
                carBody=CarBody(color=CarBodyColor.BLUE, type=CarBodyType.COMBI, components=['ABS', 'HEATING', 'GPS']),
                wheel=Wheel(model='MEGHAN', size=19, type=TyreType.SUMMER))]
        result = get_cars(self.cars)

        self.assertListEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
