my_dictionary = {}
print(type(my_dictionary))

my_dictionary = {
    'name':'Juanita',
    'lastname':'Cortez',
    'height':'165cm',
    'age' : 24,
    'sex' : 'Female',
    'occupation' : 'Flight attendant',
    'nationality' : 'Colombian',
}

print(len(my_dictionary), 'entries')
print(my_dictionary.get('name'))
print(my_dictionary.get('height'))

for dato in my_dictionary:
    print(dato, '=>', my_dictionary[dato])