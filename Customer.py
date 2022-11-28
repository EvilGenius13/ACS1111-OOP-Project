from Person import Person

class Customer(Person):
    def __init__(self, name, money, car):
        super().__init__(name)
        self.money = money
        self.car = car
    
    def quit(self):
        print(f"Fine, I'm leaving and taking my business elsewhere!")
    
    def request_car_wash(self):
        print(f"I would like to order a car wash for my {self.car}")

if __name__ == "__main__":
    test_customer = Customer('Megan', 15, "Porsche 911")
    
    print(test_customer.name)
    print(test_customer.money)
    test_customer.request_car_wash()
    test_customer.quit()