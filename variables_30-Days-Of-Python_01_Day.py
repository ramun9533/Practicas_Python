first_name =  'Francisco'
last_name = 'Poja'
country = 'Coahuila'
city = 'Monclova'
age = '500'
is_married = False
skills = ['HTML', 'CSS', 'JS', 'C/C++', 'Python']
person_info = {
    'firstname' : 'Francisco',
    'lastname' : 'Poja',
    'country' : 'Coahuila',
    'city' : 'Monclova'
}

# Printing the values stored in the variables

print('First Name: ', first_name)
print('First name length: ', len(first_name))
print('Last name: ', last_name)
print('Last name length', len(last_name))
print('Contry: ', country)
print('City: ', city)
print('Age: ', age)
print('Married', is_married)
print('Skils: ', skills)
print('Person Information: ', person_info)
#print('Person Information: ', person_info[0])
print('Skils 1: ', skills[0])

# Declaring multiple variabñes in one line

first_name, last_name, country, age, is_married = 'Pancho', 'Lopez', 'Chihuahua', 700, True

print(first_name, last_name, country, age, is_married)
print('First Name: ', first_name)
print('Last_name: ', last_name)
print('Counytry: ', country)
print('Age: ', age)
print('Married: ', is_married)
