class Vehicle:
    x = 5
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors, topSpeed):
        # calling the constructor from parent class
        super().__init__(make, color, model)
        self.doors = doors
        self.topSpeed = topSpeed


car1 =  Car("Suzuki", "Grey", "2015", 4, 200)

print(car1.make)




