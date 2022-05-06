#Exercise 5 - Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
str1='true'
str2='love'
str3=name1+name2
score=''
x=0
y=0
for char in str1:
    x+=str3.lower().count(char)
for char in str2:
    y+=str3.lower().count(char)
score=str(x)+str(y)
if int(score)>90 or int(score)<10:
    print("Your score is {}, you go together like coke and mentos.".format( score))
elif int(score)<50 and int(score)>40:
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))
