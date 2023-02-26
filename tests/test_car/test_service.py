from cars_app.car.model import Car
from cars_app.car.service import CarsService
from cars_app.car.engine.model import Engine, EngineType
from cars_app.car.car_body.model import CarBody, CarBodyColor, CarBodyType
from cars_app.car.wheel.model import Wheel, TyreType
from cars_app.car.types import SortCriteria

from decimal import Decimal

import unittest

class TestService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cars = CarsService([
            Car('AUDI', Decimal('120'), 12000, Engine(EngineType.DIESEL, 210.0),
                CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 18, TyreType.SUMMER)),
            Car('BMW', Decimal('200'), 30000, Engine(EngineType.GASOLINE, 110.0),
                CarBody(CarBodyColor.WHITE, CarBodyType.SEDAN, ['HEATING']),
                Wheel('PIRELLI', 20, TyreType.WINTER)),
            Car('VOLVO', Decimal('160'), 16000, Engine(EngineType.LPG, 140.0),
                CarBody(CarBodyColor.SILVER, CarBodyType.HATCHBACK, ['BLUETOOTH', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 15, TyreType.SUMMER))
        ])

    def test_sort_by_components_quantity(self):
        expected_result = [
            Car('BMW', Decimal('200'), 30000, Engine(EngineType.GASOLINE, 110.0),
                CarBody(CarBodyColor.WHITE, CarBodyType.SEDAN, ['HEATING']),
                Wheel('PIRELLI', 20, TyreType.WINTER)),
            Car('VOLVO', Decimal('160'), 16000, Engine(EngineType.LPG, 140.0),
                CarBody(CarBodyColor.SILVER, CarBodyType.HATCHBACK, ['BLUETOOTH', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 15, TyreType.SUMMER)),
            Car('AUDI', Decimal('120'), 12000, Engine(EngineType.DIESEL, 210.0),
                CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 18, TyreType.SUMMER))
        ]
        result = self.cars.sort_by(SortCriteria.COMPONENTS_QUANTITY)

        self.assertListEqual(result, expected_result)

    def test_sort_by_engine_power(self):
        expected_result = [
            Car('BMW', Decimal('200'), 30000, Engine(EngineType.GASOLINE, 110.0),
                CarBody(CarBodyColor.WHITE, CarBodyType.SEDAN, ['HEATING']),
                Wheel('PIRELLI', 20, TyreType.WINTER)),
            Car('VOLVO', Decimal('160'), 16000, Engine(EngineType.LPG, 140.0),
                CarBody(CarBodyColor.SILVER, CarBodyType.HATCHBACK, ['BLUETOOTH', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 15, TyreType.SUMMER)),
            Car('AUDI', Decimal('120'), 12000, Engine(EngineType.DIESEL, 210.0),
                CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 18, TyreType.SUMMER))
        ]
        result = self.cars.sort_by(SortCriteria.ENGINE_POWER)

        self.assertListEqual(result, expected_result)

    def test_sort_by_wheel_size(self):
        expected_result = [
            Car('VOLVO', Decimal('160'), 16000, Engine(EngineType.LPG, 140.0),
                CarBody(CarBodyColor.SILVER, CarBodyType.HATCHBACK, ['BLUETOOTH', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 15, TyreType.SUMMER)),
            Car('AUDI', Decimal('120'), 12000, Engine(EngineType.DIESEL, 210.0),
                CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 18, TyreType.SUMMER)),
            Car('BMW', Decimal('200'), 30000, Engine(EngineType.GASOLINE, 110.0),
                CarBody(CarBodyColor.WHITE, CarBodyType.SEDAN, ['HEATING']),
                Wheel('PIRELLI', 20, TyreType.WINTER))
        ]
        result = self.cars.sort_by(SortCriteria.WHEEL_SIZE)

        self.assertListEqual(result, expected_result)

    def test_get_cars_with_body_type_and_price_in_range(self):
        expected_result = [Car('BMW', Decimal('200'), 30000, Engine(EngineType.GASOLINE, 110.0),
                               CarBody(CarBodyColor.WHITE, CarBodyType.SEDAN, ['HEATING']),
                               Wheel('PIRELLI', 20, TyreType.WINTER))]
        result = self.cars.get_cars_with_body_type_and_price_in_range(Decimal('150'), Decimal('220'), CarBodyType.SEDAN)

        self.assertListEqual(result, expected_result)

    def test_no_cars_with_body_type_and_price_in_range(self):
        expected_result = []
        result = self.cars.get_cars_with_body_type_and_price_in_range(Decimal('250'), Decimal('280'), CarBodyType.SEDAN)

        self.assertListEqual(result, expected_result)

    @unittest.expectedFailure
    def test_incorrect_car_body_type(self):
        expected_result = []
        result = self.cars.get_cars_with_body_type_and_price_in_range(Decimal('150'), Decimal('280'), CarBodyType.HELLO)

        self.assertListEqual(result, expected_result, 'ATTRIBUTE ERROR')

    def test_incorrect_price_range(self):
        with self.assertRaises(ValueError) as e:
            self.cars.get_cars_with_body_type_and_price_in_range(Decimal('200'), Decimal('100'), CarBodyType.HATCHBACK)
        self.assertEqual('Price range is not correct', str(e.exception))

    def test_get_cars_with_engine_type(self):
        expected_result = [Car('BMW', Decimal('200'), 30000, Engine(EngineType.GASOLINE, 110.0),
                               CarBody(CarBodyColor.WHITE, CarBodyType.SEDAN, ['HEATING']),
                               Wheel('PIRELLI', 20, TyreType.WINTER))]
        result = self.cars.get_cars_with_engine_type(EngineType.GASOLINE)

        self.assertListEqual(result, expected_result)

    @unittest.expectedFailure
    def test_no_cars_with_engine_type(self):
        expected_result = []
        result = self.cars.get_cars_with_engine_type(EngineType.HELLO)

        self.assertListEqual(result, expected_result, 'ATTRIBUTE ERROR')

    def test_get_car_and_mileage(self):
        expected_result = [('BMW', 30000), ('VOLVO', 16000), ('AUDI', 12000)]
        result = self.cars.get_car_and_mileage()

        self.assertListEqual(result, expected_result)

    def test_get_wheel_type_and_cars(self):
        expected_result = {
            'SUMMER': [
                Car('AUDI', Decimal('120'), 12000, Engine(EngineType.DIESEL, 210.0),
                    CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING']),
                    Wheel('PIRELLI', 18, TyreType.SUMMER)),
                Car('VOLVO', Decimal('160'), 16000, Engine(EngineType.LPG, 140.0),
                    CarBody(CarBodyColor.SILVER, CarBodyType.HATCHBACK, ['BLUETOOTH', 'AIR CONDITIONING']),
                    Wheel('PIRELLI', 15, TyreType.SUMMER))
            ],
            'WINTER': [
                Car('BMW', Decimal('200'), 30000, Engine(EngineType.GASOLINE, 110.0),
                    CarBody(CarBodyColor.WHITE, CarBodyType.SEDAN, ['HEATING']),
                    Wheel('PIRELLI', 20, TyreType.WINTER))
            ]
        }
        result = self.cars.get_wheel_type_and_cars()

        self.assertDictEqual(result, expected_result)

    def test_get_cars_with_components(self):
        expected_result = [
            Car('AUDI', Decimal('120'), 12000, Engine(EngineType.DIESEL, 210.0),
                CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING']),
                Wheel('PIRELLI', 18, TyreType.SUMMER))
        ]
        result = self.cars.get_cars_with_components(['ABS', 'RADIO', 'AIR CONDITIONING'])

        self.assertListEqual(result, expected_result)
