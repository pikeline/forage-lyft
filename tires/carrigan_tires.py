from tires_ABC import Tires

class CarriganTires(Tires):
    def __init__(self, wear_array : list):
        self.wear_array = wear_array
    def needs_service(self) -> bool:
        for i in self.wear_array:
            if(i >= 0.9):
                return True
        return False
