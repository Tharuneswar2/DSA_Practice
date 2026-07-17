# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Initialize the parking system with the given number of big, medium, and small parking spots
        self.parking_lot = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        # Check if there are available parking spots for the given car type
        if self.parking_lot[carType] > 0:
            # If available, decrement the count and return True
            self.parking_lot[carType] -= 1
            return True
        else:
            # If not available, return False
            return False