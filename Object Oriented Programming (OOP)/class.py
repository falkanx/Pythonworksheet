# class
class Person:
    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init metodu çalıştı.')

        # methods


# object (instance)
p1 = Person(name='furkan', year= 1999) 
p2 = Person(name ='cagri', year = 2000)

# updating
p1.name = 'kemal'
p1.address = 'istanbul' 

# accessing object attributes
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)