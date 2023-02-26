from dataclasses import dataclass
from enum import Enum, auto


class CarBodyColor(Enum):
    BLACK = auto()
    SILVER = auto()
    WHITE = auto()
    RED = auto()
    BLUE = auto()
    GREEN = auto()


class CarBodyType(Enum):
    SEDAN = auto()
    HATCHBACK = auto()
    COMBI = auto()


@dataclass
class CarBody:
    color: CarBodyColor
    type: CarBodyType
    components: list[str]

    def has_all_components(self, components: list[str]) -> bool:
        return all([component in self.components for component in components])