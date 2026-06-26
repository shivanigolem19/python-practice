from abc import ABC, abstractmethod
class vehicle(ABC): 
    
    @abstractmethod 
    def start(self): 
        pass 
class car(vehicle): 
    def start(self):
        print("car engine started")
    def __init__(self):
        self.__fuel=60 
    def show(self):
        print("FUEL:",self.__fuel) 
class bike(vehicle): 
    def start(self):
        print("bike engine started")
    def __init__(self):
            self.__fuel=40
    def show(self):
        print("FUEL:",self.__fuel) 

c=car() 
c.start() 
c.show() 
d=bike() 
d.start() 
d.show()


#Updated project-1.py
from abc import ABC, abstractmethod

#Abstract Class
class Vehicle(ABC):
        
    def __init__(self, fuel):      
        self.__fuel=fuel

    @abstractmethod
    def start(self):
        pass

    def show(self):
        print("FUEL:", self.__fuel)

#Child Class-Car
class Car(Vehicle):
    def start(self):
        print("car engine started")

    def __init__(self):
        super().__init__(60)

#Child Class-Bike
class Bike(Vehicle):
    def start(self):
        print("bike engine started")

    def __init__(self):
        super().__init__(40)

#Objects 
my_car=Car()
my_bike=Bike()

#Car
my_car.start()
my_car.show()

#Bike
my_bike.start()
my_bike.show()