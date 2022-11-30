
class Car:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.gear = 'D'

    def carObject(self):
        # print(f"This is a {self.name}.")
        return(f"{self.colour} {self.name}")

# Thought I would add a function for shifting gear (e.g. shift to N for the carwash track).
    def shiftGear(self, input_gear):
        self.gear = input_gear
        print(F"The car shifts gear to {self.gear}.")

if __name__ == "__main__":
    hedwig = Car("white", "Toyota", "Rav4")
    print(hedwig.make)
    hedwig.carObject()
    hedwig.shiftGear("N")