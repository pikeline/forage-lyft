from battery.battery_ABC import Battery

class SpindlerBattery(Battery):
    '''requires last_service_date and current_date to be from the datetime class'''
    
    def __init__(self, current_date, last_service_date) -> None:
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    def needs_service(self) -> bool:
        time_difference = (self.__current_date - self.__last_service_date).days
        two_years = 730#not accounting for leap year day
        if(time_difference  > two_years):
            return True 
        else:
            return False