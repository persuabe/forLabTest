import random


class Flower:
    def __init__(self, name, cost):
        self.name = name

        self.cost = cost



    def printinfo(self):
        print(self.name, " стоит ", self.cost)


class IteratorFlower:

    def iterateFlower(self, count):
        list = ["Роза", "Тюльпан", "Пион", "Орхидея"]

        for i in list:
            f = Flower(i, random.randint(40, 70))
            f.printinfo()


def main():
    iterator = IteratorFlower();

    iterator.iterateFlower(10);


if __name__ == "__main__":
    main()