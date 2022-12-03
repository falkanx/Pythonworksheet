mylist = [1,2,3]
# myString = 'my string'

# print(len(mylist))
# print(len(myString))
# print(type(mylist))
# print(type(myString))

class ITEM():
    def __init__(self, name, maker, duration):
        self.name = name
        self.maker = maker
        self.duration = duration
        print('item objesi oluşturuldu.')

    def __str__(self):
        return f"{self.maker} tarafından {self.name} yapıldı. Dayanıklılığı {self.duration}."

    def __len__(self):
        return self.duration

    def __del__(self):
        print('item objesi silindi')

m = ITEM('Balta','Demirci',120)

# print(str(mylist))
print(str(m))
# print(len(mylist))
# print(len(m))

