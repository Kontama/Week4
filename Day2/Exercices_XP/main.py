### Exercise1
# Ensemble qui contient mes numeros favoris
my_fav_numbers = set()
my_fav_numbers = {1, 4, 9, 99, 7, 17, 77}
print("##### Numéros favoris #####")
print("Numéros : ", my_fav_numbers)
# Ajout de deux autres numeros
my_fav_numbers.add(3)
my_fav_numbers.add(11)
print("##### Numéros favoris #####")
print("Numéros : ", my_fav_numbers)
# Suppression du dernier numeros
my_fav_numbers.pop()
print("##### Numéros favoris #####")
print("Numéros : ", my_fav_numbers)
# Ensemble qui contient les numeros favoris de mon ami
friend_fav_numbers = set()
friend_fav_numbers = {7, 15, 1, 3, 25, 55, 88}
print("##### Numéros favoris de mon ami #####")
print("Numéros : ", friend_fav_numbers)
# Concatenation des deux ensemble
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Concaténation : ",our_fav_numbers)
### end exo
print("\n\n")


### Exercise2
# return Imposible car les tuples ne sont pas modifiables 
### end exo
print("\n\n")


### Exercise3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print("\t‖La liste actuelle")
print("Liste : ",basket)
basket.remove("Banana")
print("##### Suppression du mot 'Banana' de la liste #####")
print("\t‖La liste actuelle")
print("Liste : ",basket)
basket.remove("Blueberries")
print("##### Suppression du mot 'Blueberries' de la liste #####")
print("\t‖La liste actuelle")
print("Liste : ",basket)
basket.append("Kiwi")
print("##### Ajoue du mot 'Kiwi' de la liste #####")
print("\t‖La liste actuelle")
print("Liste : ",basket)
basket.append("Apples")
print("##### Ajoue du mot 'Apples' de la liste #####")
print("\t‖La liste actuelle")
print("Liste : ",basket)
# Quantité de pomme dans le panier
apples = 1
for i in basket:
    if i == "Apples":
        apples = apples + 1
print("Il y a {} pomme(s) dans le panier".format(apples))
# Vider le panier
basket.clear()
print("Panier vide",basket)
### end exo
print("\n\n")


### Exercise4
# A float a type of number. The difference is that it is more qualified as a real while the integer is a positive or negative integer.
# Float can have a comma a power
# Yes we can generate floats using operators on integers
L = list()
U = 1
for i in range(8):
    L.append(U+0.5)
    U += 0.5
print(L)
### end exo
print("\n\n")


### Exercise5
# Afficher les nombres compris de 1 à 20 
liste = list()
print("Les nombres entre 1 et 20 : ")
for i in range(1, 21):
    liste.append(i)
print("\t Liste = " + str(liste) )
print("\nLes nombres pairs entre 1 et 20 : ")
# Vider la liste
liste.clear()
# Afficher les elements pairs des nombres compris de 1 à 20
for i in range(1, 21):
    if i%2 == 0:
        liste.append(i)
print("\t Liste = " + str(liste) )
### end exo
print("\n\n")


### Exercise6
nom = ""
while nom != "Frankenstein":
    nom = input("Entrez votre nom : ")
### end exo
print("\n\n")


### Exercise7
fruits = input("Entrer vos fruits (NB:séparer les fruits avec un seul espace): ")
fruits_list  = list()
fruits_list = fruits.split()

my_fruits = input("Entrer le nom du fruit : ")
test = 0
for i in fruits_list:
    if my_fruits == i:
        test = 1

if test == 1 :
    print("Vous avez choisi l'un de vos fruits préférés! Prendre plaisir !")
else :
    print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")  
### end exo
print("\n\n")


### Exercise8
L = list()
p = 0
while True:
    pizzas = input("Entrez une garniture de pizza(s) (ou appuyez sur quitter pour annuler :")
    if pizzas != 'quit':
        L.append(pizzas)
        print("Vous ajoutez {} à la liste des garnitures de la pizza ".format(pizzas))
        p = p + 2.5
    else:
        pizzas = ""
        break      
print ( "Toutes les garnitures : " , L , " \n " , "Le prix total de cette pizza avec toutes les garnitures sont :" , 10 + p )
### end exo
print("\n\n")


### Exercise9
P=0      # price initialization
nb=int(input("Hello!! How many are you?"))  # family's numbers initialization

# Cost to pay according to the age of the family's members
for i in range(0,nb):

    age=int(input("Enter your person's age: "))
    print("Next person!")
    if age<3:
        # free ticket
        P=P+0
        
    elif 3<age<=12:
        # ticket's price is 10
        P=P+10
        
    elif age>12:
        # ticket's price is 15
        P=P+15    
 
    
print("For all (",nb,") member(s), amount is ",P)

P=0      # price initialization
nb=int(input("Hello! How many are you? : "))  # family's numbers initialization
Name=[]     # list of saved's name
k=nb
#Cost to pay according to the age of the family's members
for i in range(0,nb):
    name=input("Enter your name: ")
    age=int(input("Enter your age : "))
    Name.append(name)
    print("Saved... Pass to the next person")
    
    
    # check age

    if 16<=age<=21:
        # ticket's price is 10
        P=P+10
    else:
        # free ticket
        print("You are not allowed to watch this movie")
        k=k-1
        
        Name.remove(name) # delete the name
           
print(Name)    
print("For all (",k,") member(s), amount is ",P)
### end exo
print("\n\n")


### Exercise10
# List of sandwich
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# creation of empty list
finished_sandwiches = list()
# create "p" which will allow us to determine the exact number of sandwiches prepared
p = 0
# remove ready-made sandwiches
while sandwich_orders !=[]:
    test =input("What sandwich did you finish making?")
    if test in sandwich_orders:
        sandwich_orders.remove(test)
        finished_sandwiches.append(test)
        p = p + 1

# Print the ready-made sandwiches
for i in range(0, p):
    print("I made your",finished_sandwiches[i])
### end exo
print("\n\n")


### Exercise11
sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = list()
p = 0
print("ALERT!!! Charcuterie no longer has pastrami")


# pastramis delete
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders != [] :
    test = input("What sandwich did you finish making? ")
    if test in sandwich_orders:
        sandwich_orders.remove(test)
        finished_sandwiches.append(test)
        p = p + 1

# print the finished sandwich without pastramis
for i in range(0, p):
    print("I made your",finished_sandwiches[i])
### end exo
print("\n\n")

