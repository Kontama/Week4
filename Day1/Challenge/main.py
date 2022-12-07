###Exercise Longueur
mot = input("Saisisez votre chaine\n\t Chaine : ")
longueur = len(mot)
if(longueur<10):
    print("Chaine pas assez longue")
elif(longueur>10):
    print("Chaine trop longue")
else:
    print("Longueur de chaine exacte")
# end if
###end exo

###Exercise for
mot = "Hello World"
long = len(mot)
initial = 0
for i in range(0 , len(mot)):
    print(mot[initial   : i + 1])
#end for
###end exo