from dataclasses import dataclass
from enum import Enum, auto


class EngineType(Enum):
    DIESEL = auto()
    GASOLINE = auto()
    LPG = auto()


@dataclass
class Engine:
    type: EngineType
    power: float
