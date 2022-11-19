class Student:
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return f"I am a student. My name is {self.name}."
    def __del__(self):
        print("Training is over. I am now an expert!")

nick = Student(name="Nick")
print(nick)