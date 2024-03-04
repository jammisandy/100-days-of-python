class Animal:
    def __init__(self):
        self.num_of_eyes = 10

    def breath(self):
        print("Inhale,Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")


nemo=Fish()
nemo.swim()
nemo.breath()
print(nemo.num_of_eyes)