# Parent Class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        print(f"{self.name} protects {self.city} with {self.power}.")

# Child Class
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)  # Inherit attributes
        self.flight_speed = flight_speed

    def display_info(self):
        # Polymorphism: override the parent method
        print(f"{self.name} flies over {self.city} at {self.flight_speed} km/h using {self.power}.")

# Create objects
hero1 = Superhero("Shadow", "Invisibility", "Gotham")
hero2 = FlyingHero("SkyBolt", "Lightning", "Metropolis", 800)

hero1.display_info()  # Shadow protects Gotham with Invisibility.
hero2.display_info()  # SkyBolt flies over Metropolis at 800 km/h using Lightning.
