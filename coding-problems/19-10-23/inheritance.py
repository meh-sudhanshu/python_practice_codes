class Animal:
    def number_of_legs(self):
        print("defualt number of legs")
class FourLegAnimals:
    def number_of_legs(self):
        print(4)
class Cat(FourLegAnimals,Animal):
    def number_of_ear(self):
        print("2 ears")
cat = Cat()
cat.number_of_legs()
cat.number_of_ear()
