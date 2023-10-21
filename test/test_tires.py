import sys
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo')
sys.path.append('c:\\School\\project\\Forage\\lyft\\forage-lyft-starter-repo\\tires')
#fixes module paths

import unittest


from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class testCarrigan(unittest.TestCase):
    def test_no_service_needed(self):
        wear_array = [0.1,0.1,0.1,0.1]
        tires = CarriganTires(wear_array)
        self.assertFalse(tires.needs_service())
    def test_service_needed(self):
        wear_array = [0.1,0.1,0.1,0.9]
        tires = CarriganTires(wear_array)
        self.assertTrue(tires.needs_service())
        
class testOctoprime(unittest.TestCase):
    def test_no_service_needed(self):
        wear_array = [0.1,0.1,0.1,0.1]
        tires = CarriganTires(wear_array)
        self.assertFalse(tires.needs_service())
    def test_service_needed(self):
        wear_array = [0.75,0.75,0.75,0.75]
        tires = OctoprimeTires(wear_array)
        self.assertTrue(tires.needs_service())
        
        


if __name__ == '__main__':
    unittest.main()