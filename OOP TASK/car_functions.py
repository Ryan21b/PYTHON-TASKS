import car_data
from car_classes import Mercedes, Volkswagen, Toyota


def compile_cars_from_db():
    """
    Compiles all of the cars, based on make, split into the three classes
    :return array of cars
    """
    cars = []
    data = car_data.get_cars_based_on_make("Toyota")
    for car in data:
        cars.append(Toyota(car_id=car['id'],
                           year_model=car['year_model'],
                           distance_driven=car['distance_driven'],
                           base_price=car['base_price'],
                           tank_size=car['tank_size'],
                           kilometers_per_tank=car['kilometers_per_tank'],
                           make=car['make']))

    data = car_data.get_cars_based_on_make("Volkswagen")
    for car in data:
        cars.append(Volkswagen(car_id=car['id'],
                               year_model=car['year_model'],
                               distance_driven=car['distance_driven'],
                               base_price=car['base_price'],
                               tank_size=car['tank_size'],
                               kilometers_per_tank=car['kilometers_per_tank'],
                               make=car['make']))

    data = car_data.get_cars_based_on_make("Mercedes")
    for car in data:
        cars.append(Mercedes(car_id=car['id'],
                             year_model=car['year_model'],
                             distance_driven=car['distance_driven'],
                             base_price=car['base_price'],
                             tank_size=car['tank_size'],
                             kilometers_per_tank=car['kilometers_per_tank'],
                             make=car['make']))
    return cars


def get_car_based_on_id(cars, car_id):
    """
    :param cars: list of Car objects
    :param car_id: int
    :return: a Car object
    """
    for car in cars:
        if car.car_id == car_id:
            return car
