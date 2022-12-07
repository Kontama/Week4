###Exercise1
### end exo

###Exercise2
### end exo

###Exercise3
print(3 <= 3 < 9)
# return True
print(3 == 3 == 3)
# return True
print(bool(0))
#return False
print(bool(5 == "5"))
#return False
print(bool(4 == 4) == bool("4" == "4"))
#return True
print(bool(bool(None)))
#return False
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
#return
#   x is True
#   y is False
#   a: 5
#   b: 10
### end exo

###Exercise4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))
### end exo

###Exercise5
mot  =  str ( input ( "Entrez la phrase (sans A)\n\t Mot : " ))
while True :
    if "A" in mot :
        mot = str ( input ( "Entrez la phrase (sans A)\n\t Mot : " ))
    else :
        break
print ( "Succès tes phrases sont correctes !" )
### end exo