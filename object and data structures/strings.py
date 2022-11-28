name = 'Furkan'
surname = 'Alkan'
age = 23

greeting = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old'
length = len(greeting)

print(greeting)
print(len(greeting))
print(greeting[0])
print(greeting[3])
print(greeting[length-1])
print(greeting[-1])
print(greeting[3:7])
print(greeting[3:])
print(greeting[:16])
print(greeting[2:40:3])