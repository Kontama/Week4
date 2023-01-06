#<>

### Exercise1
def display_message():
    message = "I\'m learning python in this course"
    print(message)
display_message()
### end exo
print("\n\n")

### Exercise2
def favorite_book(title):
    print("My favorite book is "+ title)
favorite_book("One piece")
### end exo
print("\n\n")

### Exercise3
def describe_city(city, country):
    print(city + " is in " + country + ".")
describe_city('KOUDOUGOU','BURKINA')
### end exo
print("\n\n")

### Exercise4
import random

def compare_numbers(num):
    random_num = random.randint(1, 100)
    if num == random_num:
        print("Success ! Two numbers are same : " + str(num) + ".")
    else:
        print("Failed. Two numbers aren\'t same : " + str(num) + " et " + str(random_num) + ".")
compare_numbers(70)
### end exo
print("\n\n")

### Exercise5
def make_shirt(size, text):
    print("The size of the shirt is " + size + " and the text is '" + text + "'.")
      
make_shirt("medium", "I love Python")

def make_shirt(size="large", text="I love Python"):
    print("The size of the shirt is " + size + " and the text is '" + text + "'.")

make_shirt()

make_shirt(size="medium")

make_shirt(size="small", text="I love coding")
### end exo
print("\n\n")

### Exercise6
def show_magicians(names):
    for name in names:
        print(name)

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

show_magicians(magician_names)
def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + " the Great"

make_great(magician_names)

show_magicians(magician_names)
def make_great(names):
    great_names = [name + " the Great" for name in names]
    return great_names

great_magician_names = make_great(magician_names)

show_magicians(great_magician_names)
### end exo
print("\n\n")

### Exercise7
import random

def get_random_temp():
    return random.uniform(-10, 40)

for i in range(10):
    print(get_random_temp())

import random

def get_random_temp():
    return random.randint(-10, 40)


#############################################################
def main():
    # Obtaining a random temperature
    temp = (get_random_temp())
    
    print(f"The current temperature is {temp} degrees Celsius.")
    
       
main()


###############################################################################
import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temp = get_random_temp()

    if temp < 0:
        print(f"it's freezing cold! Wear extra layers today. The current temperature is {temp} degrees Celsius.")
    elif temp >= 0 and temp <= 16:
        print(f"Pretty cold! Don't forget your coat. The current temperature is {temp} degrees Celsius.")
    elif temp > 16 and temp <= 23:
        print(f"It's cool. Remember to put on a sweater. The current temperature is {temp} degrees Celsius.")
    elif temp > 23 and temp <= 32:
        print(f"The weather is nice. Don't forget to take a jacket if you go out. The current temperature is {temp} degrees Celsius.")
    elif temp > 32:
        print(f"It's hot! Don't forget to drink water and put on sunscreen. The current temperature is {temp} degrees Celsius.")

main()



################################################################

import random

def get_random_temp(saison):
    if saison == "été":
        lower_bound = 16
        upper_bound = 40
    elif saison == "automne" or saison == "printemps":
        lower_bound = -10
        upper_bound = 16
    elif saison == "hiver":
        lower_bound = -10
        upper_bound = 16
    else:

        lower_bound = -10
        upper_bound = 40

    return random.randint(lower_bound, upper_bound)

def main():

    saison = input("Enter a season (été, automne, hiver, printemps) : ")

    temp = get_random_temp(saison)
    print("The temperature is", temp, "degrees.")

main()



################bonus 1 ##############
def main():

    saison = input("Saisissez une saison (été, automne, hiver, printemps) : ")
    temp = get_random_temp(saison)
    print("La température est de", temp, "degrés.")

main()
#################################

def main():
    mois = int(input("Saisissez le numéro du mois (1-12) : "))

    if mois == 12 or mois == 1 or mois == 2:
        saison = "hiver"
    elif mois >= 3 and mois <= 5:
        saison = "printemps"
    elif mois >= 6 and mois <= 8:
        saison = "été"
    elif mois >= 9 and mois <= 11:
        saison = "automne"
    else:
        saison = "hiver"

    temp = get_random_temp(saison)
    print("La température est de", temp, "degrés.")

main()
### end exo