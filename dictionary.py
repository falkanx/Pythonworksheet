# key - value

# 41 => istanbul 34 => izmir

# sehirler = ['istanbul','izmir']
# plakalar = [41, 34]

# print(plakalar[sehirler.index('izmir')])

# print(plakalar['istanbul']) => 41
# print(plakalar['izmir']) => 34

# plakalar = { 'istanbul' : 41, 'izmir': 34 }

# print(plakalar['istanbul'])
# print(plakalar['izmir'])

# plakalar['ankara'] = 6
# plakalar['istanbul'] = 'new value'

# print(plakalar)

users = {
    'furkanalkan': {
        'age': 36,        
        'roles': ['user'],
        'email': 'furkan@gmail.com',
        'address': 'istanbul',
        'phone': '1231321'
    },
    'mustafaalkan': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'mustafa@gmail.com',
        'address': 'istanbul',
        'phone': '1231321'
    }
}

print(users['mustafaalkan']['roles'][0])



