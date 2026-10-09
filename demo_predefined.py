from vehicle import Motorcycle,Car,Truck
from price import Pricing
from garage import Level,Garage
from exceptions import ParkingException

def main():

    level1=Level("Level 1",total_spots=10)
    level2=Level("Level 2",total_spots=5)
    garage=Garage([level1,level2],Pricing())

    print("\nGarage Created")

    motorcycle=Motorcycle("motor123")
    car=Car("car456")
    truck=Truck("truck789")

    try:
        t1=garage.park(motorcycle)
        print(f"\nParked {t1}")
        t2=garage.park(car)
        print(f"\nParked {t2}")
        t3=garage.park(truck)
        print(f"\nParked {t3}")

        print(f"\nGarage filled:{garage.get_filled_percentage()}%")
        print(f"\nParked vehicles:{garage.get_parked_vehicles()}")

        print(f"\nUnparking")
        print(f"\nMotorcycle bill for 28mins:{garage.unpark(t1,28)}")
        print(f"\nCar bill for 60mins:{garage.unpark(t2,90)}")
        print(f"\nTruck bill for 90mins:{garage.unpark(t3,120)}")

    except ParkingExeption as e:
        print(f"\nParking failled:{e}")

if __name__=="__main__":
    main()
