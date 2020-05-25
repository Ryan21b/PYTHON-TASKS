import datetime


class Car:
    """
    Parent class of Toyota, Mercedes, Volkswagen

    Contains properties, calculating methods
    """
    def __init__(self, car_id, year_model, distance_driven, base_price, tank_size, kilometers_per_tank, make):
        self.car_id = car_id
        self.year_model = year_model
        self.distance_driven = distance_driven
        self.base_price = base_price
        self.tank_size = tank_size
        self.kilometers_per_tank = kilometers_per_tank
        self.make = make

    def __str__(self):
        """
        Display all of the internal data of the car
        :return: string of car info
        """
        print_str = "---Data of this car---" + '\n'
        print_str += "car_id: %s" % self.car_id + '\n'
        print_str += "year_model: %s" % self.year_model + '\n'
        print_str += "distance_driven: %s km" % self.distance_driven + '\n'
        print_str += "base_price: R%s" % self.base_price + '\n'
        print_str += "tank_size: %s L" % self.car_id + '\n'
        print_str += "kilometers_per_tank: %s km/t" % self.kilometers_per_tank
        return print_str

    def calculate_fuel_usage(self):
        """
        :return: fuel usage in kilometers/litre
        """
        return self.kilometers_per_tank/self.tank_size

    def calculate_resell_value(self):
        """
        If car is older than 20 increase price by R20k

        Calculate price by base*(0.9^age)
        :return: resell value
        """
        age_in_years = datetime.date.today().year - self.year_model
        if age_in_years >= 20:
            resell_value = self.base_price*(0.9**age_in_years) + 20000
        else:
            resell_value = self.base_price*(0.9**age_in_years)
        return resell_value


class Toyota(Car):
    slogan = "Toyota is amazing!"

    def __str__(self):
        """
        Overrides parent __str__ to adjust heading and insert slogan
        :return: string of car info
        """
        super_str = super().__str__()
        super_str += "\n" + "slogan: %s" % self.slogan
        super_str = super_str.replace("Data of this car", "Data of this Toyota")
        return super_str


class Volkswagen(Car):
    slogan = "Volkswagen is lekka!"

    def __str__(self):
        """
        Overrides parent __str__ to adjust heading and insert slogan
        :return: string of car info
        """
        super_str = super().__str__()
        super_str += "\n" + "slogan: %s" % self.slogan
        super_str = super_str.replace("Data of this car", "Data of this Volkswagen")
        return super_str


class Mercedes(Car):
    slogan = "Mercedes cars are fancy."

    def __str__(self):
        """
        Overrides parent __str__ to adjust heading and insert slogan
        :return: string of car info
        """
        super_str = super().__str__()
        super_str += "\n" + "slogan: %s" % self.slogan
        super_str = super_str.replace("Data of this car", "Data of this Mercedes")
        return super_str
