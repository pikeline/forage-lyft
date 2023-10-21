import sys
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo')
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo\\car_class')
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo\\engine')
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo\\battery')
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo\\tires')


from datetime import datetime

from car_class.Serviceable import serviceable
from car_class.car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class car_factory():
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear_array : list, tire_type : str) -> Car:
        obj = Car()
        obj.engine = CapuletEngine(current_mileage, last_service_mileage)
        obj.battery = SpindlerBattery(current_date, last_service_date)
        if(tire_type == "Carrigan"):
            obj.tires = CarriganTires(wear_array)
        elif (tire_type == "Octoprime"):
            obj.tires = OctoprimeTires(wear_array)
        return obj
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear_array : list, tire_type : str) -> Car:
        obj = Car()
        obj.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        obj.battery = SpindlerBattery(current_date, last_service_date)
        if(tire_type == "carrigan"):
            obj.tires = CarriganTires(wear_array)
        elif (tire_type == "octoprime"):
            obj.tires = OctoprimeTires(wear_array)
        return obj
    
    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on : bool, wear_array : list, tire_type : str) -> Car:
        obj = Car()
        obj.engine = SternmanEngine(warning_light_on)
        obj.battery = SpindlerBattery(current_date, last_service_date)
        if(tire_type == "Carrigan"):
            obj.tires = CarriganTires(wear_array)
        elif (tire_type == "Octoprime"):
            obj.tires = OctoprimeTires(wear_array)
        return obj
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear_array : list, tire_type : str) -> Car:
        obj = Car()
        obj.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        obj.battery = NubbinBattery(current_date, last_service_date)
        if(tire_type == "Carrigan"):
            obj.tires = CarriganTires(wear_array)
        elif (tire_type == "Octoprime"):
            obj.tires = OctoprimeTires(wear_array)
        return obj
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, wear_array : list, tire_type : str) -> Car:
        obj = Car()
        obj.engine = CapuletEngine(current_mileage, last_service_mileage)
        obj.battery = NubbinBattery(current_date, last_service_date)
        if(tire_type == "Carrigan"):
            obj.tires = CarriganTires(wear_array)
        elif (tire_type == "Octoprime"):
            obj.tires = OctoprimeTires(wear_array)
        return obj
