class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Predator(Animal):

    def eat(self, food):
        self.food = food
        print(f'{self.name} съел {food.name}')




class Mammal(Animal):
    def eat(self, food):
        self.food = food
        print(f'{self.name} съел {food.name}')


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

a1.eat(p1)
a2.eat(p2)