class Animal:
    def __init__(self, name, type, eat, age, nickname):

        '''
        :name - имя животного:
        :type - тип животного:
        :eat - чем питается:
        :age - возраст:
        :nickname - кличка:
        '''

        self.name = name
        self.type = type
        self.eat = eat
        self.age = age
        self.nickname = nickname

    def __str__(self):
        return f'Animal: {self.name}, type: {self.type}, {self.eat} \n age: {self.age}, Name: {self.nickname}'


class Bird(Animal):
    def fly(self):
        can_fly = True
        print('I believe i can fly', can_fly)


class Fish(Animal):
    def swim(self):
        can_swim = True
        print('I believe i can swim', can_swim)


class Mammals(Animal):
    def walk(self):
        can_walk = True
        print('i just walk in the empty street at nighttime', can_walk)


class Predator(Fish, Mammals, Bird):
    def eat(self):
        print('I eat the everybody who weaker then me!!!')


class Herbivores(Fish, Mammals, Bird):
    def eat(self):
        print('I love eat fresh herbs, tasty fruits, healthy vegetables')


class Falcon(Predator):
    def hunt_meta(self):
        print('i can see my victims from a great height')


class Penguin(Predator):
    def hunt_meta(self):
        print('I love swim and eat delicious fish')


class Trout(Predator):
    def eat_meta(self):
        print('im so happy when i find little fish or crabs. Idk what can i say about worm on the hook')


class Whale(Predator):
    def eat_meta(self):
        print('Food just comes in when i open my mouth')


falcon = Falcon('Bird', 'Falcon', 'Predator', 9, 'Sherhan')
print(falcon)
falcon.hunt_meta()
print('---------------------------------------------------')
penguin = Penguin('Bird', 'Penguin', 'Predator', 5, 'Roger')
print(penguin)
penguin.hunt_meta()
print('---------------------------------------------------')
trout = Trout('Fish', 'Trout', 'Predator', 1, 'Issykulskiy')
print(trout)
trout.eat_meta()
print('---------------------------------------------------')
whale = Whale('Whale', 'Whale', 'Predator', 15, 'Frank')
print(whale)
whale.eat_meta()
print('---------------------------------------------------')

