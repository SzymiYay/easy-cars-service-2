from dataclasses import dataclass
from enum import Enum, auto


class TyreType(Enum):
    WINTER = auto()
    SUMMER = auto()


@dataclass
class Wheel:
    model: str
    size: int
    type: TyreType