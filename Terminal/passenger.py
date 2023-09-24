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