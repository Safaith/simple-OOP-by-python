class car:

    def __init__(self, car_name, speed):

        self.car_Name = car_name
        self.speed_meter = speed

    def display(self):
        print("car name: ", self.car_Name)
        print("speed: ", self.speed_meter)


car1 = car("maclearn", 200)
car2 = car("ferari", 220)
car3 = car("ford", 210)
car1.display()
car2.display()
car3.display()
