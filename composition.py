class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power
        
        
class Wheel:
    def __init__(self,size):
        self.size=size
        
class Car:
    def __init__(self,make,model,horse_power,Wheel_size):
        self.make=make
        self.model=model
        self.engine=Engine(horse_power)
        self.wheel_size=[Wheel(Wheel_size) for wheel in range(4)]
    def display(self):
        return [f"Make:{self.make}   Model:{self.model}   Hourse Power:{self.engine.horse_power}   Wheel Size: {self.wheel_size[0].size} "]


        
        





    

