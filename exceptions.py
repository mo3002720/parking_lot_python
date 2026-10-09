class ParkingException(Exception):pass

class LotFullError(ParkingException):pass

class VehicleAlreadyParkedError(ParkingException):pass

class InvalidTicketError(ParkingException):pass