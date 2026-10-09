from define import SpotSize,VehicleType

class Vehicle:
    def __init__(self,Reg_num):
         self.Reg_num = Reg_num
    
    def get_size(self): raise NotImplementedError
    
    def get_type(self): raise NotImplementedError
    
    def get_spots_needed(self): 
        return 1 
    
    def can_fit_in(self,spots_group):
        if len(spots_group) != self.get_spots_needed():
            return False
        for spot in spots_group:
            if spot.size.value < self.get_size().value:
                return False
        return True

    def __eq__(self,other):
        if type(self) != type(other):
            return False
        return self.Reg_num==other.Reg_num

    def __repr__(self):
        return f"{self.__class__.__name__}(Registration_number='{self.Reg_num}')"


class Motorcycle(Vehicle):
    def get_size(self): return SpotSize.SMALL
    def get_type(self): return VehicleType.MOTORCYCLE


class Car(Vehicle):
    def get_size(self): return SpotSize.MEDIUM
    def get_type(self): return VehicleType.CAR
    

class Truck(Vehicle):
    def get_size(self): return SpotSize.LARGE
    def get_type(self): return VehicleType.TRUCK
    def get_spots_needed(self):
        return 2
    def can_fit_in(self,spots_group):
        if len(spots_group)==2:
            return True
        else:
            return False
