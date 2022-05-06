#Exercise - Banker Roulette


import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
le=len(names)
x= random.randrange(0, len(names))
char=names[x]
print("{} is going to buy the meal today!".format(char))
