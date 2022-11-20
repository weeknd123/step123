import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 5
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.03
        self.gladness -= 3
    def to_sleep(self):
        print("I will sleep")
        self.gladness +=5
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 3
    def to_work(self):
        print("Time to go work")
        self.money += 5
        self.progress +=0.1
        self.gladness -= 3



    def is_alive(self):
        if self.money <= -3:
            self.to_work()
        elif self.progress <= -0.3:
            self.to_study()
        elif self.progress < -0.5:
            print("Cast Out...")
            self.alive = False
        elif self.gladness <=0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money < -5:
            print("Broke")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        live_cube = random.randint(1,4)
        if live_cube == 1 or live_cube == 2 :
            self.to_study()
        elif live_cube == 3:
            self.to_sleep()
        elif live_cube == 4:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Cristiano")
for day in range(365):
    if nick.alive ==  False:
        break
    nick.live(day)

