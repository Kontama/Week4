###Exercise1
# Create my first list
first_l = [1, 2, 3, 4, 5, 6]
second_l = [11, 22, 33, 44, 55, 66]
first_l.extend(second_l)
print("", first_l)
### end exo

###Exercise2
for i in range(1500, 2500) :
    # Verify is i is a multiple of 5 and 7
    if ((i%5 == 0) and (i%7 == 0)):
        print(i)
### end exo


###Exercise3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
pt = 0
name = input('Enter your name : ')
for i in names:
    if (i == name):
        pt = 0       
if pt != 0:
    print("Your name {} is in position {} ".format(name, pt))
else :
    print("Your name is not on the list")
### end exo