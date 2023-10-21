from Serviceable import serviceable


class Car(serviceable):
    
    def __init__(self):
        self.engine = ""
        self.battery = ""
        self.tires = ""
        
    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()