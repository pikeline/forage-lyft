from Serviceable import serviceable


class Car(serviceable):
    
    def __init__(self):
        self.engine = ""
        self.battery = ""
        
    def needs_service(self) -> bool:
        return engine.needs_service() or battery.needs_service()