from Person import Person

class Clerk(Person):
    def __init__(self, name, weekend_shift = False):
        super().__init__(name)
        self._amount_owed = 0
        self._weekend_shift = weekend_shift

    def greet(self):
        print(f"Hi I'm {self.name}. Are you here for a car wash?")
    
    def quit(self):
        print(f"Looks like my shift is over! Time to go home.")

    def what_shift(self):
        if self._weekend_shift == True:
            print(f"Yeah it's my turn to work the weekend...")
        else:
            print(f"Yay I have the weekend off!")
    
if __name__ == "__main__":
    test_clerk = Clerk("Darius")
    test_clerk.greet()
    test_clerk.what_shift()
    test_clerk.hand.append("Car Keys")
    print(test_clerk.hand)

