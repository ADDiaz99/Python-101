my_dictionary = {}
print(type(my_dictionary))

my_dictionary = {
    'name':'Nicky',
    'apellio' : 'Miranda',
    'estado_mental' : 'dudoso xd',
    'edad' : '21', 
    'secso' : 'femenino' 
      
}

print(len(my_dictionary), 'datos')
print(my_dictionary.get('secso'))
for dato in my_dictionary:
    print(dato, '=>', my_dictionary[dato])