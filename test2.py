class Foo:
    def __init__(self, name, age ):
        self.name = name
        #self.age = age
        self._age = age

obj = Foo('alix',19)
print(obj.name)
print(obj._age)
