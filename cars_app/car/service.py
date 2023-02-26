from .model import Car
from .car_body.model import CarBodyType
from .engine.model import EngineType
from .wheel.model import TyreType
from .types import SortCriteria

from dataclasses import dataclass
from decimal import Decimal
from collections import defaultdict


@dataclass
class CarsService:
    cars: list[Car]

    def sort_by(self, sort_criteria: SortCriteria, *, reverse=False) -> list[Car]:
        match sort_criteria:
            case SortCriteria.COMPONENTS_QUANTITY:
                return sorted(self.cars, key=lambda car: len(car.carBody.components), reverse=reverse)
            case SortCriteria.ENGINE_POWER:
                return sorted(self.cars, key=lambda car: car.engine.power, reverse=reverse)
            case _:
                return sorted(self.cars, key=lambda car: car.wheel.size, reverse=reverse)

    def get_cars_with_body_type_and_price_in_range(self, price_from: Decimal, price_to: Decimal,
                                                   body_type: CarBodyType):
        if price_from > price_to:
            raise ValueError('Price range is not correct')

        return [car for car in self.cars if
                car.carBody.type == body_type and car.has_price_between(price_from, price_to)]

    def get_cars_with_engine_type(self, engine_type: EngineType) -> list[Car]:
        return [car for car in self.cars if car.engine.type == engine_type]

    def get_statistics(self) -> str:
        return f"""
                PRICE:
                average: {sum([car.price for car in self.cars]) / len(self.cars)}
                max: {max(self.cars, key=lambda car: car.price).price}
                min: {min(self.cars, key=lambda car: car.price).price}

                MILEAGE:
                average: {sum([car.mileage for car in self.cars]) / len(self.cars)}
                max: {max(self.cars, key=lambda car: car.mileage).mileage}
                min: {min(self.cars, key=lambda car: car.mileage).mileage}

                ENGINE POWER:
                average: {sum([car.engine.power for car in self.cars]) / len(self.cars)}
                max: {max(self.cars, key=lambda car: car.engine.power).engine.power}
                min: {min(self.cars, key=lambda car: car.engine.power).engine.power}
                """

    def get_car_and_mileage(self) -> list[tuple[Car, int]]:
        return sorted([(car.model, car.mileage) for car in self.cars], key=lambda pair: pair[1], reverse=True)

    def get_wheel_type_and_cars(self) -> dict[TyreType, list[Car]]:
        wheel_type_and_cars = defaultdict(list)

        for car in self.cars:
            wheel_type_and_cars[car.wheel.type.name].append(car)

        return dict(wheel_type_and_cars)

    def get_cars_with_components(self, components: list[str]) -> list[Car]:
        return [car for car in self.cars if car.has_all_components(components)]

    def __str__(self):
        to_string = [str(car) for car in self.cars]
        return '\n'.join(to_string)
