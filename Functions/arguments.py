# def changeName(n):
#     n = 'cagri'

# name = 'kemal'

# changeName(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# sehirler = ['ankara','izmir']

# change(sehirler[:])

# print(sehirler)

def add(*params):
    print(type(params))
    sum = 0
    for n in params:
        sum = sum + n
    return sum

print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30,50,60,10,20))

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name= 'furkan', age = 2, city = 'istanbul')
displayUser(name= 'cagri', age = 12, city = 'kocaeli', phone = '123132')
displayUser(name= 'kemal', age = 14, city = 'ankara', phone = '123132', email= 'kemal@gmail.com')

def myFunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')

