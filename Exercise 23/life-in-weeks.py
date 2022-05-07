#Exercise - Life in Weeks

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import datetime
diff= 90-int(age)
print("You have {} days, {} weeks, and {} months left.".format(diff*365,diff*52,diff*12))
