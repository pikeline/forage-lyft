from abc import ABC, abstractmethod

class serviceable(ABC):
    '''The serviceable ABC that ensures all Cars implement needs_service()'''
    @abstractmethod
    def needs_service(self) -> bool:
        pass