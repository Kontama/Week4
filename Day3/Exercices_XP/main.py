#<>

### Exercise1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)
### end exo
print("\n\n")

### Exercise2
family = {}

while True:
    name = input("Input a name (or tape 'done' to quit) : ")
    if name == 'done':
        break
    age = int(input("Input the person\'s name : "))
    family[name] = age

total_cost = 0

for name, age in family.items():
    if age < 3:
        cost = 0
    elif age >= 3 and age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{name} must paid {cost}$ for the ticket.")
    total_cost += cost

print(f"The total price of the tickets is {total_cost}$.")
### end exo
print("\n\n")

### Exercise3
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }
}

brand['number_stores'] = 2

print(f"Zara's customers are men, women, children and those looking for home furnishings.")

brand['country_creation'] = 'Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

del brand['creation_date']

print(f"The last international competitor's is {brand['international_competitors'][-1]}.")

print(f"The major colors in the US are {', '.join(brand['major_color']['US'])}.")

print(f"The amount of key value pairs is {len(brand)}")

print(f"The keys of the dictionary are : {', '.join(brand.keys())}.")

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

brand.update(more_on_zara)

print(f"The number of Zara stores is now {brand['number_stores']}.")
### end exo
print("\n\n")

### Exercise4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}

for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)

disney_users_B = {}

for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)

disney_users_C = {}

for user in sorted(users):
    disney_users_C[user] = users.index(user)
print(disney_users_C)

disney_users_D = {}

for user in users:
    if 'i' in user:
        disney_users_D[user] = users.index(user)
print(disney_users_D)

disney_users_E = {}

for user in users:
    if user.startswith(('m', 'p')):
        disney_users_E[user] = users.index(user)
print(disney_users_E)
### end exo