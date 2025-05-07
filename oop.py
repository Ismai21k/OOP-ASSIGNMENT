
# Superhero Class with Inheritance

class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Origin: {self.origin}")

    def attack(self):
        print(f"{self.name} uses their power: {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def attack(self):
        print(f"{self.name} soars through the sky and strikes at {self.flight_speed} km/h!")

class StrengthHero(Superhero):
    def __init__(self, name, power, origin, strength_level):
        super().__init__(name, power, origin)
        self.strength_level = strength_level

    def attack(self):
        print(f"{self.name} smashes with strength level {self.strength_level}!")

# Example usage
hero1 = FlyingHero("Skybolt", "Flight", "Planet Zephyria", 800)
hero2 = StrengthHero("Titan", "Super Strength", "Earth", 9000)

hero1.display_info()
hero1.attack()

print()

hero2.display_info()
hero2.attack()
