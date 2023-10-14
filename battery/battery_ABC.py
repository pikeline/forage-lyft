from abc import ABC, abstractmethod

class Battery(ABC):
    '''the abstract class for batteries
    must implement needs_service(self)'''
    @abstractmethod
    def needs_service(self) -> None:
        pass