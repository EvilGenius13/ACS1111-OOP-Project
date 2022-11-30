from Clerk import Clerk
from Car import Car

class CarWash:
    def __init__(self, name, open_till_amount = 350):
        self.name = name
        self.open_till_amount = open_till_amount
        self.current_till_amount = open_till_amount
        self.list_of_cars_washed = list()
        self.cars_washed = len(self.list_of_cars_washed)
        self.clerks_on_shift = list()
          

    def store_front(self):
        print(f"Welcome to {self.name}! See clerk to wash car.")

    def create_clerk(self):
        name = input("Clerk's Name: ")
        weekend_shift = input(f"Is {name} working this weekend? ")
        return Clerk(name, weekend_shift)      

    def add_clerk_to_shift(self, name):
        shift = input(f"what shift is {name} working? ")
        self.clerks_on_shift.append({name: shift})

    def create_car(self):
        name = input("Car make and model: ")
        colour = input("car's colour? ")
        return Car(name, colour)

    def wash_car(self):
        car = self.create_car()
        print(f"Washing {car.carObject()}")
        self.cars_washed += 1
        self.current_till_amount += 10
        self.list_of_cars_washed.append(car.carObject())


if __name__ == "__main__":
    marios = CarWash("Mario's Super Wash", 1050)
    print(marios)

    clerk1 = marios.create_clerk()
    marios.add_clerk_to_shift(clerk1.name)
    clerk2 = marios.create_clerk()
    marios.add_clerk_to_shift(clerk2.name)
    print()
    print("Clerks on shift today:")
    for clerk in marios.clerks_on_shift:
        print(clerk)
    print()

    marios.wash_car()
    marios.wash_car()
    marios.wash_car()
    marios.wash_car()
    print()
    print("Cars washed so far:")
    for car in marios.list_of_cars_washed:
        print(car)
    print()

    print("Number of cars washed: " + str(marios.cars_washed))
    print("Current till amount: $"+ str(marios.current_till_amount))