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