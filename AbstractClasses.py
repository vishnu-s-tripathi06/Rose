from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(this):
        pass
    def stop(this):
        pass
class Car(Vehicle):
    def __init__(this,name):
         this.name=name   
    def go(this):
        print(f"{this.name} is start.")
    def stop(this):
        print(f"{this.go} is stop.")
class Bike(Vehicle):
    def go(this):
        print(f"{this.name} is bike.")
    def stop(this):
        print(f"{this.go} is ride.")
       

    
gadi=Car("honda")
gadi.go()


