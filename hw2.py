import random
class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_eat(self):
        print("Time to eat")
        self.progress -= 0.16
        self.gladness += 3
    def to_sleep(self):
        print("I will sleep")
        self.gladness +=3
    def to_cuddles(self):
        print("Cuddles")
        self.gladness += 5
        self.progress += 0.3

    def is_alive(self):
        if self.progress < -0.5:
            print("Dumb Cat...")
            self.alive = False
        elif self.gladness <=0:
            print("Sad Cat...")
            self.alive = False
        elif self.progress > 5:
            print("Cat died...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 3:
            self.to_sleep()
        elif live_cube == 4:
            self.to_cuddles()
        self.end_of_day()
        self.is_alive()

cat = Cat(name="Louis")
for day in range(365):
    if cat.alive ==  False:
        break
    cat.live(day)