# Smart Parking System:
# • Create classes Vehicle, ParkingSpot, and ParkingLot.
# • Create multiple objects (vehicles, spots, parking lot).
# • Demonstrate object creation, attribute initialization, and method calls.
# • Make sensitive attributes private (e.g., license plate, owner name, spot status).
# • Provide getter/setter methods to access/update them safely.
# • Show that direct access fails but methods work.
# • Vehicle is the base class.
# • Derived classes:
# Bike (extra attribute: helmet_required)
# Car (extra attribute: seats)
# SUV (extra attribute: four_wheel_drive)
# Truck (extra attribute: max_load_capacity)
# • Each child class overrides display() to print its own details.
# • Create a list of different vehicle objects (Bike, Car, SUV, Truck).
# • Iterate and call display() → each object responds differently.
# • Implement a calculate_parking_fee() method:
# Bike → ₹20/hour
# Car → ₹50/hour
# SUV → ₹70/hour
# Truck → ₹100/hour
# • Demonstrate runtime polymorphism by calling the method on different objects.
# • Create an abstract class/interface Payment (using abc module).
# • Define an abstract method process_payment(amount).
# • Create child classes:
# CashPayment
# CardPayment
# UPIPayment
# • Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).
# Task 1: Vehicle Classes
# Implement base and derived vehicle classes with encapsulation.
# Override display() and calculate_parking_fee().
# Task 2: ParkingSpot Class
# Implement ParkingSpot with size restrictions (S, M, L, XL).
# Methods: assign_vehicle(), remove_vehicle().
# Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
# Task 3: ParkingLot Class
# Store multiple parking spots.
# Methods:
# add_spot() → add new parking spots.
# show_spots() → display all spots and their status.
# park_vehicle(vehicle) → find suitable spot and park.
# unpark_vehicle(vehicle) → remove from spot and calculate fee.
# Task 4: Payment (Abstraction + Polymorphism)
# When un-parking a vehicle, calculate fee (based on hours).
# Ask user for payment method → process payment using appropriate child class.
# Task 5: Main Program
# Create a parking lot with mixed spots.
# Create multiple vehicle objects.
# Park/unpark vehicles.
# Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.


# class Vehicle:
#     def __init__(self,licenceplate,ownername,spotstatus):
#         self.__licenceplate=licenceplate
#         self.__ownername=ownername
#         self.__spotstatus=spotstatus
#     # Getters
#     def get_licenceplate(self):
#         return self.__licenceplate

#     def get_ownername(self):
#         return self.__ownername

#     def get_spotstatus(self):
#         return self.__spotstatus
#     #setters
#     def set_spotstatus(self, status):
#         self.__spotstatus = status

#     # To be overridden by child classes
#     def display(self):
#         print("Vehicle:", self.__licenceplate, self.__ownername, self.__spotstatus)

#     def calculate_parking_fee(self, hours):
#         return 0   # Default, overridden by child
# class Bike(Vehicle):
#         def __init__(self,licenceplate,ownername,spotstatus,helmet_required):
#             super().__init__(licenceplate,ownername,spotstatus)
#             self.helmet_required=helmet_required
#         def display(self):
#             print(f"Bike → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, Helmet: {self.helmet_required}")

#         def calculate_parking_fee(self, hours):
#             return 20 * hours
    
# class Car(Vehicle):
#         def __init__(self,licenceplate,ownername,spotstatus,seats):
#             super().__init__(licenceplate,ownername,spotstatus)
#             self.seats=seats  
#         def display(self):
#             print(f"Car → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, Seats: {self.seats}")

#         def calculate_parking_fee(self, hours):
#             return 50 * hours
# class SUV(Vehicle):
#         def __init__(self,licenceplate,ownername,spotstatus,four_wheel_drive):
#             super().__init__(licenceplate,ownername,spotstatus)
#             self.four_wheel_drive=four_wheel_drive 
#         def display(self):
#             print(f"SUV → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, 4WD: {self.four_wheel_drive}")

#         def calculate_parking_fee(self, hours):
#             return 70 * hours
# class Truck(Vehicle):
#         def __init__(self,licenceplate,ownername,spotstatus,max_load_capacity):
#             super().__init__(licenceplate,ownername,spotstatus)
#             self.max_load_capacity=max_load_capacity 
#         def display(self):
#             print(f"Truck → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, Load: {self.max_load_capacity}kg")

#         def calculate_parking_fee(self, hours):
#             return 100 * hours
# ##
# proc=[Bike(),Car(),SUV(),Truck()]
# for i in proc:
#       print()

#   #calculate parkinng fee...
#   def calculate_parking_fee():
                    



# class ParkingSpot:


# class ParkingLot:


# vehicles=Vehicle()
# spots=ParkingSpot()
# lot=ParkingLot()















from abc import ABC, abstractmethod
import datetime

class Vehicle:
    def __init__(self, licenceplate, ownername):
        self.__licenceplate = licenceplate
        self.__ownername = ownername
        self.__spotstatus = "Free"

    # Getters & Setters
    def get_licenceplate(self):
        return self.__licenceplate

    def get_ownername(self):
        return self.__ownername

    def get_spotstatus(self):
        return self.__spotstatus

    def set_spotstatus(self, status):
        self.__spotstatus = status

    # To be overridden
    def display(self):
        print(f"Vehicle: {self.__licenceplate}, Owner: {self.__ownername}, Status: {self.__spotstatus}")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, licenceplate, ownername, helmet_required):
        super().__init__(licenceplate, ownername)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, Helmet: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, licenceplate, ownername, seats):
        super().__init__(licenceplate, ownername)
        self.seats = seats

    def display(self):
        print(f"Car → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, licenceplate, ownername, four_wheel_drive):
        super().__init__(licenceplate, ownername)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, licenceplate, ownername, max_load_capacity):
        super().__init__(licenceplate, ownername)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck → Plate: {self.get_licenceplate()}, Owner: {self.get_ownername()}, Load: {self.max_load_capacity}kg")

    def calculate_parking_fee(self, hours):
        return 100 * hours


# parking spot
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size  # S, M, L, XL
        self.__occupied = False
        self.vehicle = None
        self.start_time = None

    def is_occupied(self):
        return self.__occupied

    def assign_vehicle(self, vehicle):
        if self.__occupied:
            print(f"Spot {self.spot_id} already occupied.")
            return False
        # Size validation
        if not self.check_fit(vehicle):
            print(f"Vehicle {vehicle.get_licenceplate()} does not fit in spot {self.spot_id} ({self.size})")
            return False
        self.vehicle = vehicle
        self.__occupied = True
        vehicle.set_spotstatus("Occupied")
        self.start_time = datetime.datetime.now()
        print(f"Vehicle {vehicle.get_licenceplate()} parked at Spot {self.spot_id}")
        return True

    def remove_vehicle(self):
        if not self.__occupied:
            print(f"Spot {self.spot_id} is already empty.")
            return None, 0
        end_time = datetime.datetime.now()
        hours = max(1, int((end_time - self.start_time).total_seconds() // 3600))  # at least 1 hour
        vehicle = self.vehicle
        self.vehicle = None
        self.__occupied = False
        self.start_time = None
        vehicle.set_spotstatus("Free")
        return vehicle, hours

    def check_fit(self, vehicle):
        # Bike → S+, Car → M+, SUV → L+, Truck → XL only
        if isinstance(vehicle, Bike):
            return self.size in ["S", "M", "L", "XL"]
        elif isinstance(vehicle, Car):
            return self.size in ["M", "L", "XL"]
        elif isinstance(vehicle, SUV):
            return self.size in ["L", "XL"]
        elif isinstance(vehicle, Truck):
            return self.size == "XL"
        return False


# parking lot 
class ParkingLot:
    def __init__(self):
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def show_spots(self):
        for spot in self.spots:
            status = "Occupied" if spot.is_occupied() else "Free"
            print(f"Spot {spot.spot_id} ({spot.size}) → {status}")

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if not spot.is_occupied() and spot.check_fit(vehicle):
                return spot.assign_vehicle(vehicle)
        print(f"No available spot for vehicle {vehicle.get_licenceplate()}")
        return False

    def unpark_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                v, hours = spot.remove_vehicle()
                fee = v.calculate_parking_fee(hours)
                print(f"Parking Fee for {v.get_licenceplate()} ({hours} hrs): ₹{fee}")
                self.process_payment(fee)
                return
        print("Vehicle not found in parking lot.")

    def process_payment(self, amount):
        print("Choose payment method: 1. Cash  2. Card  3. UPI")
        choice = input("Enter choice: ")
        if choice == "1":
            CashPayment().process_payment(amount)
        elif choice == "2":
            CardPayment().process_payment(amount)
        else:
            UPIPayment().process_payment(amount)


#payment abstraction
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in Cash ✅")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via Card 💳")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI 📱")


#main prog
if __name__ == "__main__":
    # Create parking lot
    lot = ParkingLot()
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "L"))
    lot.add_spot(ParkingSpot(4, "XL"))

    # Create vehicles
    bike = Bike("TS09AB1234", "Nithin", True)
    car = Car("TS09CD5678", "Bharath", 4)
    suv = SUV("TS09EF9101", "Akhil", True)
    truck = Truck("TS09GH1122", "Raj", 5000)

    # Park vehicles
    lot.park_vehicle(bike)
    lot.park_vehicle(car)
    lot.park_vehicle(suv)
    lot.park_vehicle(truck)

    lot.show_spots()

    # Unpark (demonstrate fee + payment)
    lot.unpark_vehicle(car)

