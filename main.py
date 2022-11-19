class Student:
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return f"I am a student. My name is {self.name}."

nick = Student(name="Nick")
print(nick)