from cars_app.car.car_body.model import CarBody
from cars_app.car.car_body.model import CarBodyColor
from cars_app.car.car_body.model import CarBodyType

import unittest
import pytest


class TestCarBody(unittest.TestCase):

    def test_has_all_components(self):
        car_body = CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING'])
        result = car_body.has_all_components(['ABS', 'RADIO', 'AIR CONDITIONING'])

        self.assertTrue(result)

    def test_has_not_all_components(self):
        car_body = CarBody(CarBodyColor.BLACK, CarBodyType.HATCHBACK, ['ABS', 'RADIO', 'AIR CONDITIONING'])
        result = car_body.has_all_components(['HEATING', 'RADIO', 'AIR CONDITIONING'])

        self.assertFalse(result)