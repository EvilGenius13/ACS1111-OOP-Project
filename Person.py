import random

class Person(object):
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def greet(self):
        print(f"Hi, my name is {self.name}.")
    
    def quit(self):
        print(f"I'm going home.")



if __name__ == "__main__":
    test_person = Person('Nick')
    test_person_1 = Person('Lisa')
    
    print(test_person.name)
    test_person_1.greet()
    test_person.quit()