class Foo:
    def __init__(self,name,age):

        self.name = name
        self.age = age

    def __iter__(self):
        return iter([11,22,33,44])
li = Foo('ALIX',12)
print(li.name)

for i in li:
    print(i)

print(li.__iter__)