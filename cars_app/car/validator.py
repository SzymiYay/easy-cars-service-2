from cars_app.validator.text import matches_regex, has_only_upper
from .engine.model import EngineType
from .wheel.model import TyreType
from .car_body.model import CarBodyColor, CarBodyType
from ..logger.model import MyLogger

from typing import Any


def validate_car_data(car_data: dict[str, Any]) -> bool:
    errors = {
        'car': car_data['model'],
        'model': _validate_car_model(car_data),
        'price': _validate_car_price(car_data),
        'mileage': _validate_car_mileage(car_data),
        'engine': _validate_car_engine(car_data),
        'carBody': _validate_car_body(car_data)
    }

    logger_validator = MyLogger.get_logger()

    if len(errors['model']) != 0 or \
            len(errors['price']) != 0 or \
            len(errors['mileage']) != 0 or \
            len(errors['engine']) != 0 or \
            len(errors['carBody']) != 0:
        logger_validator.error(', '.join([f'{k}: {v}' for k, v in errors.items()]))
        return False

    return True


def _validate_car_model(car_data: dict[str, Any]) -> list[str]:
    if 'model' not in car_data:
        return ['Required']

    errors = []
    car_model = car_data['model']

    if not has_only_upper(car_model):
        errors.append('Must contain only uppercase letters')

    return errors


def _validate_car_price(car_data: dict[str, Any]) -> list[str]:
    if 'price' not in car_data:
        return ['Required']

    errors = []
    car_price = car_data['price']

    if not matches_regex(r'^\d+(\.\d+)?$', str(car_price)):
        errors.append('Must be decimal value')

    if car_price < 0:
        errors.append('Must be greater than zero')

    return errors


def _validate_car_mileage(car_data: dict[str, Any]) -> list[str]:
    if 'mileage' not in car_data:
        return ['Required']

    errors = []
    car_mileage = car_data['mileage']

    if car_mileage < 0:
        errors.append('Must be greater than zero')

    return errors


def _validate_car_engine(car_data: dict[str, Any]) -> list[str]:
    if 'engine' not in car_data:
        return ['Required']

    errors = []
    car_engine = car_data['engine']
    engine_type = car_engine['type']
    engine_power = car_engine['power']

    engine_types = [t.name for t in EngineType]

    if engine_type not in engine_types:
        errors.append(f'Permitted types {", ".join(engine_types)}')

    if not matches_regex(r'^\d+(\.\d+)?$', str(engine_power)):
        errors.append('Must be decimal value')

    if engine_power < 0:
        errors.append('Must be greater than zero')

    return errors


def _validate_car_body(car_data: dict[str, Any]) -> list[str]:
    if 'carBody' not in car_data:
        return ['Required']

    errors = []
    car_body = car_data['carBody']
    car_body_color = car_body['color']
    car_body_type = car_body['type']
    car_body_components = car_body['components']

    car_body_colors = [c.name for c in CarBodyColor]
    car_body_types = [t.name for t in CarBodyType]

    if car_body_color not in car_body_colors:
        errors.append(f'Permitted types {", ".join(car_body_colors)}')

    if car_body_type not in car_body_types:
        errors.append(f'Permitted types {", ".join(car_body_types)}')

    for component in car_body_components:
        if not has_only_upper(component):
            errors.append('Must contain only uppercase letters')

    return errors


def _validate_car_wheel(car_data: dict[str, Any]) -> list[str]:
    if 'wheel' not in car_data:
        return ['Required']

    errors = []
    car_wheel = car_data['wheel']
    wheel_type = car_wheel['type']
    wheel_model = car_wheel['model']
    wheel_size = car_wheel['size']

    wheel_types = [t.name for t in TyreType]

    if wheel_type not in wheel_types:
        errors.append(f'Permitted types {", ".join(wheel_types)}')

    if not has_only_upper(wheel_model):
        errors.append('Must contain only uppercase letters')

    if wheel_size < 0:
        errors.append('Must be greater than zero')

    return errors
