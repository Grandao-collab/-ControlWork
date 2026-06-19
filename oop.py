class Person:
    def __init__(self):
        self._age = None

    def set_age(self, age):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = age

    def get_age(self):
        return self._age


class Creature:
    def __init__(self, nickname):
        self.nickname = nickname

    def speak(self):
        return "I am a creature"


class Dog(Creature):
    def speak(self):
        return "Woof"


class Cat(Creature):
    def speak(self):
        return "Meow"


class Transport:
    def move(self):
        return "Transport is moving"


class Car(Transport):
    def move(self):
        return "Car is driving"


class Bicycle(Transport):
    def move(self):
        return "Bicycle is pedaling"


def move(vehicle):
    return vehicle.move()


from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


if __name__ == "__main__":
    person = Person()
    person.set_age(25)
    print(person.get_age())

    dog = Dog("Rex")
    cat = Cat("Murka")
    print(dog.nickname, dog.speak())
    print(cat.nickname, cat.speak())

    car = Car()
    bike = Bicycle()
    print(move(car))
    print(move(bike))

    rect = Rectangle(8, 4)
    circle = Circle(6)
    print(rect.area())
    print(circle.area())
