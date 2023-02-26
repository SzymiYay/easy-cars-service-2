from .engine.model import Engine, EngineType
from .wheel.model import Wheel, TyreType
from .car_body.model import CarBody, CarBodyType, CarBodyColor

from dataclasses import dataclass
from typing import Any
from decimal import Decimal


@dataclass
class Car:
    model: str
    price: Decimal
    mileage: int
    engine: Engine
    carBody: CarBody
    wheel: Wheel

    def has_price_between(self, price_from: Decimal, price_to: Decimal) -> bool:
        return price_from <= self.price <= price_to

    def has_all_components(self, components: list[str]) -> bool:
        return self.carBody.has_all_components(components)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> 'Car':
        car = Car(**data)
        car.price = Decimal(data['price'])

        car.engine = Engine(**data['engine'])
        car.engine.type = EngineType[data['engine']['type']]

        car.carBody = CarBody(**data['carBody'])
        car.carBody.color = CarBodyColor[data['carBody']['color']]
        car.carBody.type = CarBodyType[data['carBody']['type']]

        car.wheel = Wheel(**data['wheel'])
        car.wheel.type = TyreType[data['wheel']['type']]

        return car

    def __str__(self):
        return f"""
        MODEL: {self.model}
        PRICE: {self.price}
        MILEAGE: {self.mileage}
        ENGINE: {self.engine.type.name}, {self.engine.power}
        CAR BODY: {self.carBody.color.name}, {self.carBody.type.name}, {self.carBody.components}
        WHEEL: {self.wheel.type.name}, {self.wheel.model}, {self.wheel.size}
        """
