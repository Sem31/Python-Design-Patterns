import string
import random


class VehicleInfo:

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02

        # compute the payable tax
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:

    def __init__(self, vehicle_id, license_plate, info):
        self.vehicle_id = vehicle_id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.vehicle_id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    def __init__(self):
        self.vehicle_info = {}
        self.add_vehicle_info("TATA Nexon", True, '13,00,000')
        self.add_vehicle_info("Volkswagen ID3", True, 35000)

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        id = self.generate_vehicle_id(12)
        vehicle_license = self.generate_vehicle_license(id)
        return Vehicle(id, vehicle_license, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()
        vehicle = registry.create_vehicle(brand)

        vehicle.print()

app = Application()
app.register_vehicle("Volkswagen ID3")