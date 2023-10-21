import sys
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo')
#fixes module paths

import unittest
from datetime import datetime

from factory.CarFactory import car_factory
from car_class.car import Car

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class TestSpindler(unittest.TestCase):
    def test_battery_no_service(self):
        today = datetime.today()
        last_service_date = today.replace(year = today.year - 1)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())
    
    def test_battery_3_years_exact(self):
        today = datetime(4,1,1)
        three_year_gap = datetime(1,1,1)
        battery = SpindlerBattery(today, three_year_gap)
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
        
if __name__ == '__main__':
    unittest.main()