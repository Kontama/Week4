#<>

### Exercise1
print("Hello world\n" *4)
### end exo

### Exercise2
cal = (99^3) * 8
print(cal)
### end exo

### Exercise3
print(5<3)
    #return false 
print(3==3)
    #return true
print(3=="3")
    #return false
print("3">3)
    #return typeError
print("Hello"=="hello")
    #return false
### end exo

### Exercise4
computer_brand = "Hp EliteBook"
print("I have a <" + computer_brand + "> computer.")
### end exo

### Exercise5
name = "Paré Léandre Bénilde"
age = 20
shoe_size = 44
info = "Hello je suis Paré Léandre Bénilde, j'ai 20ans, j'aime bien regarder les animés manga et je shots du 44."
print(info)
### end exo

### Exercise6
a = input("Entrer un nombre a = ")
b = input("Entrer un nombre b = ")
if(a>b):
    print("Hello world!")
# end if
### end exo

### Exercise7
parity = int (input("Entrer un nombre :\n\t\t nombre = "))
if((parity % 2)==0):
    print("Le nombre",parity,"saisie est pair!")
else:
    print("Le nombre",parity,"saisie est impair!")
#end if
### end exo

### Exercise8
computer = "aomine"
user = input("Comment t'appelles-tu ?\n\t\t Nom = ")
if(user==computer):
    print("Salut cousin, sois le bienvenu !!")
else:
    print("Désolé mais vous avez un nom pourru 😁😁!!")
# end if
### end exo

### Exercise9
taille = int(input("Combien mesurez-vous ? \n\t\t Taille(en cm) = "))
if(taille >= 145):
    print("Vous avez ",taille,"cm")
    print("Bravo!! Vous êtes assez grand, vous avez le droit de rouler\n")
else:
    print("Vous avez ",taille,"cm")
    print("Désolé!! Vous devez grandir un peu plus avant de pouvoir rouler\n")
### end exo

