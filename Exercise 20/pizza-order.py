#Exercise - Pizza Order

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
Pizza_size_price={'S':15,'M':20,'L':25}
Pizza_add_pepperoni={'S':2, 'M':3, 'L':3}
Pizza_add_extra_cheese=1
if add_pepperoni=='Y' and extra_cheese=='Y':
    bill+=Pizza_size_price[size]+Pizza_add_pepperoni[size]+Pizza_add_extra_cheese
    print("Your final bill is: ${}.".format(bill))
elif add_pepperoni=='N' and extra_cheese=='Y':
    bill+=Pizza_size_price[size]+Pizza_add_extra_cheese
    print("Your final bill is: ${}.".format(bill))
elif add_pepperoni=='Y' and extra_cheese=='N':
    bill+=Pizza_size_price[size]+Pizza_add_pepperoni[size]
    print("Your final bill is: ${}.".format(bill))
else:
    bill+=Pizza_size_price[size]
    print("Your final bill is: ${}.".format(bill))
