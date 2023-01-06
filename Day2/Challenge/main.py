###Exercise 
num = int(input("Entrer un number : "))
print("\n")
leng = int(input("Entrer un lenght : "))

dico = []

for x in range (1, leng+1):
    dico.append(num*x) 
print(dico)
###end exo

###Exercise for
string = input("Input a string : ")

new_string = ""

for i in range(len(string)):
  if i == 0 or string[i] != string[i-1]:
    new_string += string[i]

print(new_string)
###end exo