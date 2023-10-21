import sys
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo')
#fixes module paths

import unittest
from datetime import datetime

from factory.CarFactory import car_factory
from car_class.car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


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
        
if __name__ == '__main__':
    unittest.main()