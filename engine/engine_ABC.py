from abc import ABC, abstractmethod

class Engine(ABC):
    '''the abstract class for engines
    must implement needs_service(self)'''
    @abstractmethod
    def needs_service(self) -> bool:
        pass