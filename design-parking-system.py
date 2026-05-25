class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Initialize the parking system with the given number of big, medium, and small spots
        self.spots = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        # Check if there are available spots for the given car type
        if self.spots[carType] > 0:
            # If available, decrement the count and return True
            self.spots[carType] -= 1
            return True
        else:
            # If not available, return False
            return False

# Example usage:
parking_system = ParkingSystem(2, 3, 4)
print(parking_system.addCar(1))  # True
print(parking_system.addCar(2))  # True
print(parking_system.addCar(3))  # True
print(parking_system.addCar(1))  # True
print(parking_system.addCar(2))  # True
print(parking_system.addCar(3))  # True
print(parking_system.addCar(1))  # False