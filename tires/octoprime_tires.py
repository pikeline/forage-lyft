from tires_ABC import Tires

class OctoprimeTires(Tires):
    def __init__(self, wear_array : list):
        self.wear_array = wear_array
    def needs_service(self) -> bool:
        total_wear = 0
        for i in self.wear_array:
            total_wear += i
        return total_wear >= 3