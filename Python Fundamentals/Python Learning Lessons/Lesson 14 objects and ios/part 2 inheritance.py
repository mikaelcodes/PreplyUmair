class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        pass  # Each subclass will implement its own version of speak()


class Dog(Animal):
    def __init__(self, name):
        super().__init__('Dog')
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def __init__(self, name):
        super().__init__('Cat')
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"


# Creating instances of Dog and Cat
dog = Dog('Buddy')
cat = Cat('Whiskers')

# Using the speak method of each object
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
