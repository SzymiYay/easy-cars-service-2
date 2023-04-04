#### <p align="center">The project is currently in the development phase, and new features are being added!</p>
---

# CAR SERVICE

The project takes data from a json file. Then from the console we have the ability to manage cars.
Project written in learning Python, JSON, data management, data validation and testing. 

I plan to add a database layer and UI (FastAPI, Flask).


## Built With
- Python
- Pytest
- Unittest
- Poetry
- MySQL
- Docker


## Getting Started
1. Clone the repo
   ```sh
   git clone https://github.com/SzymiYay/easy-cars-service-2
   ```
2. To start the project, you need to have Python and Poetry installed on your computer.
3. Set on the project directory.
4. Run application:
   ```sh
   poetry run pyhton -m cars_app
   ```
5. Run tests:
   ```sh
   pytest
   ```
   
## Usage
Example JSON:
```json
[
    {
    "model": "BMW",
    "price": 160,
    "mileage": 25000,
    "engine": {
      "type": "LPG",
      "power": 250.0
    },
    "carBody": {
      "color": "GREEN",
      "type": "SEDAN",
      "components": [
        "ABS",
        "HEATING"
      ]
    },
    "wheel": {
      "type": "WINTER",
      "model": "X6",
      "size": 21
    }
  }
]
```

From the json file, download the data. Then, using the get_cars function to validate the data, 
place it in an array and create a CarsService object.
Having such an object, you can manage the data in various ways

```python
def main() -> None:
   FILENAME: Final[str] = 'cars_app/data/cars.json'
   cars_data = get_cars_data_json(FILENAME)
   cars = get_cars(cars_data)
   cars_service = CarsService(cars)

   print(cars_service.get_cars_with_body_type_and_price_in_range(Decimal('100'), Decimal('170'), CarBodyType.SEDAN))
   print(cars_service.get_cars_with_engine_type(EngineType.DIESEL))
   print(cars_service.get_statistics())

```


## Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new-feature`)
3. Commit your Changes (`git commit -m 'Add some new-feature'`)
4. Push to the Branch (`git push origin feature/new-feature`)
5. Open a Pull Request


## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact
Szymon Frączek - szymoon09@gmail.com
