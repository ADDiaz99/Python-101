print("--- "*5)
person= {
  'name': 'Camilo',
  'last_name': 'Rico',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name']='Camilo Andres'
person['age']-=50
person['langs'].append('rust')
print(person)
del person['last_name']
person.pop('age')
print(person)


print(person.items())
print(person.keys())
print(person.values())
print(person.clear())



person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29,
    'twitter': '@nicobytes',
}

# Escribe tu solución 👇
person['name'] = 'Felipe'
person['age'].pop

print(person)
