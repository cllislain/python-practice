bus_fare_matrix = {
    "Taft": 20.0,
    "Magallanes": 30.0,
    "Ayala": 40.0,
    "Buendia": 50.0,
    "Guadalupe": 60.0
}

taxi_fare_matrix = {
    "Taft": 70.0,
    "Magallanes": 80.0,
    "Ayala": 90.0,
    "Buendia": 100.0,
    "Guadalupe": 110.0
}

class Vehicle:
    vehicle_counters = {"BUS": 0, "TAXI": 0}
    
    def __init__(self, vehicle_type, max_capacity, fare_matrix):
        self.vehicle_type = vehicle_type
        self.vehicle_id = f"{vehicle_type}{Vehicle.get_next_vehicle_number(vehicle_type)}"
        self.max_capacity = max_capacity
        self.passengers = []
        self.fare_matrix = fare_matrix

    def get_vehicle_id(self):
        return self.vehicle_id

    def board_passenger(self, passenger):
        if len(self.passengers) < self.max_capacity:
            self.passengers.append(passenger)
            return True
        else:
            return False

    def get_last_destination(self):
        if self.passengers:
            return self.passengers[-1].get_last_destination()
        return None
    
    @classmethod
    def get_next_vehicle_number(cls, vehicle_type):
        cls.vehicle_counters[vehicle_type] += 1
        return cls.vehicle_counters[vehicle_type]


class Bus(Vehicle):
    def __init__(self):
        super().__init__("BUS", max_capacity=3, fare_matrix=bus_fare_matrix)


class Taxi(Vehicle):
    def __init__(self):
        super().__init__("TAXI", max_capacity=1, fare_matrix=taxi_fare_matrix)


class Passenger:
    passenger_counters = {"REG": 0, "SENPWD": 0}
    
    def __init__(self, passenger_type, initial_budget):
        self.passenger_type = passenger_type
        self.passenger_id = f"{passenger_type}{Passenger.get_next_passenger_number(passenger_type)}"
        self.initial_budget = initial_budget
        self.wallet_balance = initial_budget
        self.travel_log = []

    def get_passenger_id(self):
        return self.passenger_id

    def get_wallet_balance(self):
        return self.wallet_balance

    def get_last_destination(self):
        if self.travel_log:
            return self.travel_log[-1]
        return None

    def deduct_fare(self, fare):
        if self.wallet_balance >= fare:
            self.wallet_balance -= fare
            return True
        return False

    def record_travel(self, destination):
        self.travel_log.append(destination)
    
    @classmethod
    def get_next_passenger_number(cls, passenger_type):
        cls.passenger_counters[passenger_type] += 1
        return cls.passenger_counters[passenger_type]


class RegularPassenger(Passenger):
    def __init__(self, initial_budget):
        super().__init__("REG", initial_budget)
        
    def load_wallet(self, amount):
        self.wallet_balance += amount

class SeniorPWDPassenger(Passenger):
    def __init__(self, initial_budget):
        super().__init__("SENPWD", initial_budget)

    def load_wallet(self, amount):
        self.wallet_balance += amount    

class CommuterTerminal:
    def __init__(self):
        self.passengers = []
        self.vehicles = []

    def main(self):
        while True:
            print("\n[ Menu ]")
            print("1. Register Passenger")
            print("2. Load Passenger Wallet")
            print("3. Show Passenger Wallet Balance")
            print("4. Show Fare Matrix")
            print("5. Show Available Vehicles")
            print("6. Show Passenger Counts")
            print("7. Board a Vehicle")
            print("8. Show Travel Log")
            print("9. Exit\n")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.register_passenger()
            elif choice == "2":
                self.load_wallet()
            elif choice == "3":
                self.show_wallet_balance()
            elif choice == "4":
                self.show_fare_matrix()
            elif choice == "5":
                self.show_available_vehicles()
            elif choice == "6":
                self.show_passenger_counts()
            elif choice == "7":
                self.board_vehicle()
            elif choice == "8":
                self.show_travel_log()
            elif choice == "9":
                print("\nThank You and Have a Nice Day...")
                break
            else:
                print("\nInvalid choice. Choose from 1-9")

    def register_passenger(self):
        passenger_type = input("Enter passenger type (REG/SENPWD): ").upper()
        initial_budget = float(input("Enter initial budget: "))
        
        if passenger_type == "REG":
            passenger = RegularPassenger(initial_budget)
        elif passenger_type == "SENPWD":
            passenger = SeniorPWDPassenger(initial_budget)
        else:
            print("Invalid passenger type.")
            return
        
        self.passengers.append(passenger)
        print(f"Passenger registered with ID: {passenger.get_passenger_id()}")
        
    def load_wallet(self):
        passenger_id = input("Enter passenger ID: ")
        passenger = self.find_passenger(passenger_id)
        
        if passenger:
            amount = float(input(f"Enter the amount to load into {passenger_id}'s wallet: "))
            passenger.load_wallet(amount)
            print(f"Wallet of {passenger_id} loaded with P{amount:.1f}. New balance: P{passenger.get_wallet_balance():.1f}")
        else:
            print("Passenger not found.")

    def show_wallet_balance(self):
        passenger_id = input("Enter passenger ID: ")
        passenger = self.find_passenger(passenger_id)
        
        if passenger:
            print(f"Wallet balance for passenger {passenger_id}: P{passenger.get_wallet_balance():.1f}")
        else:
            print("Passenger not found.")

    def show_fare_matrix(self):
        vehicle_type = input("Enter vehicle type (BUS/TAXI): ").upper()
        fare_matrix = bus_fare_matrix if vehicle_type == "BUS" else taxi_fare_matrix
        print(f"***** {vehicle_type} Fare Matrix *****")
        for destination, fare in fare_matrix.items():
            print(f"{destination}: P{fare:.1f}")
        print("*" * (len(vehicle_type) + 14))

    def show_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.vehicles:
            print(f"{vehicle.vehicle_type} {vehicle.vehicle_id}")

    def show_passenger_counts(self):
        regular_count = sum(1 for passenger in self.passengers if isinstance(passenger, RegularPassenger))
        senpwd_count = sum(1 for passenger in self.passengers if isinstance(passenger, SeniorPWDPassenger))
        print("Passenger Counts:")
        print(f"Regular Passengers: {regular_count}")
        print(f"Senior/PWD Passengers: {senpwd_count}")
        
    def board_vehicle(self):
        passenger_id = input("Enter passenger ID: ")
        passenger = self.find_passenger(passenger_id)
        
        if not passenger:
            print("Passenger not found.")
            return
        
        vehicle_type = input("Enter vehicle type (BUS/TAXI): ").upper()
        

        vehicle = self.find_available_vehicle(vehicle_type)
        if not vehicle:
            if vehicle_type == "BUS":
                vehicle = Bus()
            elif vehicle_type == "TAXI":
                vehicle = Taxi()
            else:
                print("Invalid vehicle type.")
                return
            self.vehicles.append(vehicle)
        
        print(f"Available destinations for {vehicle.get_vehicle_id()}:")
        for destination, fare in vehicle.fare_matrix.items():
            print(f"{destination}: P{fare:.1f}")
        
        destination = input("Enter your destination: ")
        fare = vehicle.fare_matrix.get(destination, 0)  # Default to 0 if destination is not found
        
        if fare > passenger.get_wallet_balance():
            print(f"Passenger {passenger.get_passenger_id()} does not have enough fare to board {vehicle.get_vehicle_id()}!")
        else:
            if vehicle.board_passenger(passenger):
                passenger.deduct_fare(fare)
                passenger.record_travel(destination)
                print(f"Passenger {passenger.get_passenger_id()} successfully boarded {vehicle.get_vehicle_id()} with a fare of P{fare:.1f}")
            else:
                print(f"Vehicle {vehicle.get_vehicle_id()} is already full.")

    def show_travel_log(self):
        passenger_id = input("Enter passenger ID: ")
        passenger = self.find_passenger(passenger_id)
        
        if passenger:
            travel_log = " | ".join(passenger.travel_log)
            print(f"[{passenger_id}] Wallet Balance: {passenger.get_wallet_balance()} | Travel Log: [{travel_log}]")
        else:
            print("Passenger not found.")

    def show_summary(self):
        num_vehicles = len(self.vehicles)
        num_buses = sum(1 for vehicle in self.vehicles if isinstance(vehicle, Bus))
        num_taxis = num_vehicles - num_buses
        num_passengers = len(self.passengers)
        num_regular_passengers = sum(1 for passenger in self.passengers if isinstance(passenger, RegularPassenger))
        num_senpwd_passengers = num_passengers - num_regular_passengers
        
        print("[ LOG ]")
        print(f"Number of Vehicles: {num_vehicles}")
        print(f"Number of Buses: {num_buses}")
        print(f"Number of Taxis: {num_taxis}")
        print(f"Number of Passengers: {num_passengers}")
        print(f"Number of Regular Passengers: {num_regular_passengers}")
        print(f"Number of Senior/PWD Passengers: {num_senpwd_passengers}")
    
    def find_passenger(self, passenger_id):
        for passenger in self.passengers:
            if passenger.get_passenger_id() == passenger_id:
                return passenger
        return None

    def find_available_vehicle(self, vehicle_type):
        for vehicle in self.vehicles:
            if vehicle.vehicle_type == vehicle_type and len(vehicle.passengers) < vehicle.max_capacity:
                return vehicle
        return None

if __name__ == "__main__":
    terminal = CommuterTerminal()
    terminal.main()
