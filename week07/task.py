from abc import ABCMeta
class Zoo(object):
    def __init__(self,name):
        self.name = name
        self.animals = []
    def add_animal(self,animal):
        if self.has_animal(animal) :
            pass
        else:
            self.animals.append(animal)
            setattr(self, animal.__class__.__name__, None)
    def has_animal(self,animal):
        for added in self.animals:
            if id(added) == id(animal):
                return True
        return False
class Animal(metaclass=ABCMeta):
    def __init__(self,type_animal,body,character):
        self.type = type_animal
        self.body = body
        self.character = character
        if body != "小" and type_animal == "食肉" and character == "凶猛":
            self.is_ferocity = True
        else:
            self.is_ferocity = False
class Cat(Animal):
    bark = "meow"
    def __init__(self,name,type_animal,body,characte):
        self.name = name
        super().__init__(type_animal,body,characte)
        if self.is_ferocity:
            self.is_pet = False
        else:
            self.is_pet = True
class Dog(Animal):
    bark = "woo"
    def __init__(self,name,type_animal,body,characte):
        self.name = name
        super().__init__(type_animal,body,characte)
        if self.is_ferocity:
            self.is_pet = False
        else:
            self.is_pet = True   
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)