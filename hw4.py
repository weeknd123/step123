class Car:
    def __init__(self, year, make, model, **kwargs):
        super().__init__(**kwargs)
        self.year = year
        self.make = make
        self.model = model

class Engine:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = "Engine: 6.0-litre V12 engine"

class Audi(Car, Engine):
    def print_info(self):
        print(self.year)
        print(self.make)
        print(self.model)
        print(self.engine)

audi = Audi(model = "R8", year="2023", make="Audi")
audi.print_info()
