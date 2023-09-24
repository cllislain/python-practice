bus_fare_matrix = {
    "Taft": 20.0,
    "Magallanes": 30.0,
    "Ayala": 40.0,
    "Buendia": 50.0,
    "Guadalupe": 60.0,
}

taxi_fare_matrix = {
    "Taft": 70.0,
    "Magallanes": 80.0,
    "Ayala": 90.0,
    "Buendia": 100.0,
    "Guadalupe": 110.0,
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
    passenger_counters = {"BUS": 0, "TAXI": 0}
    
    def __init__(self, passenger_type, initial_budget):
        self.passenger_type = passenger_type
        self.passenger_id
        self.initial_budget = initial_budget
        