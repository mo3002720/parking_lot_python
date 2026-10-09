from exceptions import LotFullError,VehicleAlreadyParkedError,InvalidTicketError
from define import SpotSize

class Spot:

    def __init__(self,size):
        self.size=size
        self.is_free=True
    
    def __repr__(self):
        return f"Spot({self.size.name},free={self.is_free})"


class Level:

    def __init__(self,name,total_spots):
        self.name=name
        self.spots=self.generate_spots(total_spots)

    def generate_spots(self,total):
        small_spots=int(total*0.40)
        medium_spots=int(total*0.40)
        large_spots=total-small_spots-medium_spots

        spots_list=[]
        for i in range(small_spots):
            spots_list.append(Spot(SpotSize.SMALL))
        for i in range(medium_spots):
            spots_list.append(Spot(SpotSize.MEDIUM))
        for i in range(large_spots):
            spots_list.append(Spot(SpotSize.LARGE))
        return spots_list

    def __len__(self):
        free_count=0
        for spot in self.spots:
            if spot.is_free==True:
                free_count = free_count+1
        return free_count


class Ticket:
    counter=0

    @classmethod
    def generate_ticket(cls):
        cls.counter = cls.counter+1
        return f"Ticket-{cls.counter}"

    def __init__(self,vehicle,spots):
        self.id=self.generate_ticket()
        self.vehicle=vehicle
        self.spots=spots
        self.is_active=True

    def __str__(self):
        return f"Ticket {self.id} for {self.vehicle.Reg_num}"

class Garage:

    def __init__(self,levels,pricing_sys):
        self.levels=levels
        self.pricing_sys=pricing_sys
        self.active_tickets={}

    def park(self,vehicle):
        if vehicle.Reg_num in self.active_tickets:
            raise VehicleAlreadyParkedError("Vehicle is already parked")

        needed=vehicle.get_spots_needed()
        for level in self.levels:
            for j in range(len(level.spots)-needed+1):
                group=level.spots[j:j+needed]
                spots_are_free=True
                for spot in group:
                    if spot.is_free==False:
                        spots_are_free=False
                if spots_are_free==True:
                    if vehicle.can_fit_in(group)==True:
                        for spot in group:
                            spot.is_free=False
                        ticket=Ticket(vehicle,group)
                        self.active_tickets[vehicle.Reg_num]=ticket
                        return ticket
        raise LotFullError("No avialable spots")


    def unpark(self,ticket,minutes):
        if ticket.is_active==False:
            raise InvalidTicketError("Ticket already used")
        if ticket.vehicle.Reg_num not in self.active_tickets:
            raise InvalidTicketError("Ticket not found")
        for spot in ticket.spots:
            spot.is_free=True

        ticket.is_active=False
        del self.active_tickets[ticket.vehicle.Reg_num]
        return self.pricing_sys.bill(ticket.vehicle,minutes)

    def get_filled_percentage(self):
        total_spots=0
        free_spots=0
        for level in self.levels:
            for spot in level.spots:
                total_spots=total_spots+1
                if spot.is_free==True:
                    free_spots=free_spots+1
        if total_spots==0:
            return 0.0
        taken_spots=total_spots-free_spots
        return (taken_spots/total_spots)*100
    def get_parked_vehicles(self):
        vehicle_list=[]
        for ticket in self.active_tickets.values():
            vehicle_list.append(ticket.vehicle)
        return vehicle_list
    