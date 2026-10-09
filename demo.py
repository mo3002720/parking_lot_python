from vehicle import Motorcycle,Car,Truck
from price import Pricing
from garage import Level,Garage
from exceptions import ParkingException

def main():
    levels_str=input("\nEnter number of level in the garage:")
    num_levels=int(levels_str)

    levels_list=[]
    for i in range(num_levels):
        spots_str=input(f"\nEnter total spots for level {i+1}:")
        total_spots=int(spots_str)
        levels_list.append(Level(f"Level {i+1}", total_spots))

    garage=Garage(levels_list,Pricing())
    print(f"\nGarage created with {num_levels} levels.")

    count_str=input("\nNumber of vehicles:")
    num_vehicles=int(count_str)

    saved_tickets=[]
    for i in range(num_vehicles):
        Reg_num=input(f"\nEnter registration number for vehicle {i+1}:")
        print("\nMotorcycle=1 ; Car=2 ; Truck=3")
        v_type=input("\nEnter vehicle code:")

        if v_type=='1':
            vehicle=Motorcycle(Reg_num)
        elif v_type=='2':
            vehicle=Car(Reg_num)
        elif v_type=='3':
            vehicle=Truck(Reg_num)
        else:
            print("\nInvalid code")
            continue

        try:
            ticket=garage.park(vehicle)
            saved_tickets.append(ticket)
            print(f"\nParked {ticket}")
        except ParkingException as e:
            print(f"\nParking failed:{e}")

    print(f"\nGarage Fullness:{garage.get_filled_percentage()}%")

    print(f"\nUNPARKING")
    for ticket in saved_tickets:
        time_str=input(f"\nEnter parked time in minutes for {ticket.vehicle.Reg_num}:")
        minutes=int(time_str)

        try:
            price=garage.unpark(ticket,minutes)
            print(f"\n{ticket.vehicle.Reg_num} bill amout:{price}")
        except ParkingException as e:
            print(f"\nUnparking failed: {e}")


if __name__=="__main__":
    main()