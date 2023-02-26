from cars_app.data_loader.json_loader import get_cars_data_json
from cars_app.car.model import Car
from cars_app.car.service import CarsService
from cars_app.car.engine.model import Engine, EngineType
from cars_app.car.car_body.model import CarBody, CarBodyColor, CarBodyType
from cars_app.car.wheel.model import Wheel, TyreType

from decimal import Decimal

import pytest
import unittest


class TestJsonLoader(unittest.TestCase):

    def test_get_cars_data_json(self):
        expected_result = [
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
        result = get_cars_data_json('cars_app/data/cars.json')

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
