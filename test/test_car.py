import sys
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo')
#fixes module paths

import unittest
from datetime import datetime

from factory.CarFactory import car_factory
from car_class.car import Car

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestSpindler(unittest.TestCase):
    def test_battery_no_service(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_battery_2_years_exact(self):
        today = datetime(3,1,1)
        two_year_gap = datetime(1,1,1)
        battery = SpindlerBattery(today, two_year_gap)
        self.assertFalse(battery.needs_service())
    
    def battery_needs_service(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
        
class TestNubbin(unittest.TestCase):
    def test_battery_no_service(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_battery_4_years_exact(self):
        today = datetime(5,1,1)
        four_year_gap = datetime(1,1,1)
        battery = NubbinBattery(today, four_year_gap)
        self.assertTrue(battery.needs_service())
    
    def battery_needs_service(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
        
class TestCapulet(unittest.TestCase):
    def less_than_30k_miles(self):
        current = 29999
        last_mileage = 0
        engine = CapuletEngine(current, last_mileage)
        self.assertFalse(engine.needs_service())
    
    def exactly_30k_miles(self):
        current = 30000
        last_mileage = 0
        engine = CapuletEngine(current, last_mileage)
        self.assertFalse(engine.needs_service())
        
    def greater_than_30k_miles(self):
        current = 30001
        last_mileage = 0
        engine = CapuletEngine(current, last_mileage)
        self.assertTrue(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def less_than_60k_miles(self):
        current = 59999
        last_mileage = 0
        engine = WilloughbyEngine(current, last_mileage)
        self.assertFalse(engine.needs_service())
    
    def exactly_60k_miles(self):
        current = 60000
        last_mileage = 0
        engine = WilloughbyEngine(current, last_mileage)
        self.assertFalse(engine.needs_service())
        
    def greater_than_60k_miles(self):
        current = 60001
        last_mileage = 0
        engine = WilloughbyEngine(current, last_mileage)
        self.assertTrue(engine.needs_service())
        
class TestSternman(unittest.TestCase):
    def test_warning_light_on(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
        
    def test_warning_light_off(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())
    

class TestCalliope(unittest.TestCase):
    def test_no_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 29999
        last_mileage = 0
        car = car_factory.create_calliope(today, last_service_date, current, last_mileage)
        self.assertFalse(car.needs_service())
        
    def test_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        current = 29999
        last_mileage = 0
        car = car_factory.create_calliope(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 30001
        last_mileage = 0
        car = car_factory.create_calliope(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_and_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        current = 30001
        last_mileage = 0
        car = car_factory.create_calliope(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_no_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 29999
        last_mileage = 0
        car = car_factory.create_glissade(today, last_service_date, current, last_mileage)
        self.assertFalse(car.needs_service())
        
    def test_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        current = 29999
        last_mileage = 0
        car = car_factory.create_glissade(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 60001
        last_mileage = 0
        car = car_factory.create_glissade(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_and_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        current = 60001
        last_mileage = 0
        car = car_factory.create_glissade(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_no_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        warning_light_on = False
        car = car_factory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertFalse(car.needs_service())
        
    def test_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        warning_light_on = False
        car = car_factory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())
        
    def test_engine_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        warning_light_on = True
        car = car_factory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())
        
    def test_engine_and_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 3)
        warning_light_on = True
        car = car_factory.create_palindrome(today, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_no_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 29999
        last_mileage = 0
        car = car_factory.create_rorschach(today, last_service_date, current, last_mileage)
        self.assertFalse(car.needs_service())
        
    def test_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 5)
        current = 29999
        last_mileage = 0
        car = car_factory.create_rorschach(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 60001
        last_mileage = 0
        car = car_factory.create_rorschach(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_and_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 5)
        current = 60001
        last_mileage = 0
        car = car_factory.create_rorschach(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_no_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 29999
        last_mileage = 0
        car = car_factory.create_thovex(today, last_service_date, current, last_mileage)
        self.assertFalse(car.needs_service())
        
    def test_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 5)
        current = 29999
        last_mileage = 0
        car = car_factory.create_thovex(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        current = 30001
        last_mileage = 0
        car = car_factory.create_thovex(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())
        
    def test_engine_and_battery_service_needed(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 5)
        current = 30001
        last_mileage = 0
        car = car_factory.create_thovex(today, last_service_date, current, last_mileage)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()