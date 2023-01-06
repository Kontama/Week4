###Exercise
# Instructs the user to enter a sequence of words separated by commas
words = input("Saisissez une séquence de mots séparés par des virgules : ")

words_list = [word.strip() for word in words.split(',')]

words_list.sort()

print(', '.join(words_list))
# end if
###end exo