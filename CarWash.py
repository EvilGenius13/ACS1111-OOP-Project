

class CarWash:
    def __init__(self, name, open_till_amount = 350):
        self.name = name
        self.open_till_amount = open_till_amount
        self.current_till_amount = open_till_amount
        self.cars_washed = 0
        self.clerks_on_shift = list()


    def store_front(self):
        print(f"Welcome to {self.name}! See clerk to wash car.")

    def create_clerk(self, name):
        pass

    def add_clerk_to_shift():
        pass


