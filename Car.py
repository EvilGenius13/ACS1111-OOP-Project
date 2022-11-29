
class Car:
    def __init__(self, colour, make, model):
        self.colour = colour
        self.make = make
        self.model = model
        self.gear = 'D'

    def carObject(self):
        print(f"This is a {self.colour} {self.make} {self.model}.")
        return(f"{self.colour} {self.make} {self.model}")

# Thought I would add a function for shifting gear (e.g. shift to N for the carwash track).
    def shiftGear(self, gear):
        self.gear = gear
        print(F"The car shifts gear to {self.gear}.")

if __name__ == "__main__":
    hedwig = Car("white", "Toyota", "Rav4")
    hedwig.carObject()
    hedwig.shiftGear("N")