# Polymorphism Challenge with Vehicles

class Vehicle:
    def move(self):
        print("The vehicle moves.")

class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Example usage
vehicles = [Car(), Plane(), Boat()]

print("\nVehicle Movements:")
for v in vehicles:
    v.move()

