class Animal:
    def __init__(self, name, speak):
        print("Constructing Animal")
        self.name = name
        self.speak = speak

    def animal_speak(self):
        print(str(self.name) + " is " + str(self.speak))

dog = Animal("Dog", "BARKING")
dog.animal_speak()
