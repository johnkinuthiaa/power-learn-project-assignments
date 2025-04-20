# activity one
class Animal:
    def __init__(self,animal_type,name,breed,color):
        self.name=name
        self.animal_type=animal_type
        self.breed=breed
        self.color=color
    def to_string(self):
        print(f"Name:{self.name}\nbreed:{self.breed}\nColor:{self.color}")
    def walk(self):
        print(f"The {self.name} is walking")
    def get_color(self):
        print(f"its a {self.color} {self.animal_type}")

tommy =Animal("Dog","Tommy","Bulldog","brown")
tommy.to_string()
tommy.walk()

class Dog(Animal):
    def __init__(self, animal_type, name, breed, color):
        super().__init__(animal_type, name, breed, color)

    def walk(self):
        print("the dog is walking")

tommy =Dog("Dog","Tommy","Bulldog","brown")

tommy.walk()

# challenge 2

class Vessel:

    def __init__(self,name):
        self.name=name
    def move(self):
        print("the vessel is moving")
class Car(Vessel):
    def __init__(self,name):
        super().__init__(name)
    def move(self):
        print(f"The {self.name} is driving away")
class Plane(Vessel):
    def __init__(self,name):
        super().__init__(name)
    def move(self):
        print(f"The {self.name} is flying away")

plane =Plane("plane")
car =Car("car")

plane.move()
car.move()

