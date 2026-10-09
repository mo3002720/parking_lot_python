import math
from define import VehicleType

class Pricing:
    RATE = {
        VehicleType.MOTORCYCLE:5.0,
        VehicleType.CAR:10.0,
        VehicleType.TRUCK:15.0,
    }

    @staticmethod
    def bill(vehicle,minutes):
        if minutes <= 30:
            return 0.0
        hours = math.ceil(minutes/60.0)
        return hours*Pricing.RATE[vehicle.get_type()]