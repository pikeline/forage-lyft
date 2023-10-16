from datetime import datetime

from car_class.car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory():
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        obj = Car()
        obj.engine = CapuletEngine(current_mileage, last_service_mileage)
        obj.battery = SpindlerBattery(current_date, last_service_date)
        return obj
    
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        obj = Car()
        obj.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        obj.battery = SpindlerBattery(current_date, last_service_date)
        return obj
    
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on : bool) -> Car:
        obj = Car()
        obj.engine = SternmanEngine(warning_light_on)
        obj.battery = SpindlerBattery(current_date, last_service_date)
        return obj
    
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        obj = Car()
        obj.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        obj.battery = NubbinBattery(current_date, last_service_date)
        return obj
    
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        obj = Car()
        obj.engine = CapuletEngine(current_mileage, last_service_mileage)
        obj.battery = NubbinBattery(current_date, last_service_date)
        return obj