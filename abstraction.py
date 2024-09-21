
class car:
    def __init__(self):
        self.speed=30

    def accelerate(self):
        self.speed+=10
        print(self.speed)

    def brakk(self):
        self.speed-=10
        print(self.speed)

    def drive(self):
        self.accelerate()


obj=car()
obj.drive()
