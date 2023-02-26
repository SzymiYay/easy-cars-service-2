from cars_app.car.model import Car
from cars_app.car.engine.model import Engine, EngineType
from cars_app.car.car_body.model import CarBody, CarBodyColor, CarBodyType
from cars_app.car.wheel.model import Wheel, TyreType

from decimal import Decimal

import unittest


class TestCar(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.car = Car(
            'AUDI',
            Decimal('120'),
            12000,
            Engine(EngineType.DIESEL, 210.0),
            CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'AIR CONDITIONING']),
            Wheel('PIRELLI', 18, TyreType.SUMMER)
        )

    def test_price_in_range(self):
        result = self.car.has_price_between(Decimal('100'), Decimal('140'))
        self.assertTrue(result)

    def test_price_not_in_range(self):
        result = self.car.has_price_between(Decimal('200'), Decimal('300'))
        self.assertFalse(result)

    def test_has_all_components(self):
        components = ['ABS', 'AIR CONDITIONING']
        result = self.car.has_all_components(components)

        self.assertTrue(result)

    def test_has_not_all_components(self):
        components = ['ABS', 'AIR CONDITIONING', 'HEATING']
        result = self.car.has_all_components(components)

        self.assertFalse(result)

    def test_from_dict(self):
        car = {
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
        }
        result = Car.from_dict(car)

        self.assertEqual(result, self.car)
