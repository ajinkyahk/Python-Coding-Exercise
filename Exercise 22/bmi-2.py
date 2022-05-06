#Exercise - BMI 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import math
bmi=(float(weight)/float(height)**2)
bmi=math.ceil(bmi)
if bmi<18.5:
    print("Your BMI is {}, you are underrweight.".format(bmi))
elif bmi>18.5 and bmi<25:
    print("Your BMI is {}, you have a normal weight.".format(bmi))
elif bmi>25 and bmi<30:
    print("Your BMI is {}, you are slightly overweight.".format(bmi))
elif bmi>30 and bmi<35:
    print("Your BMI is {}, you are obese.".format(bmi))
else: 
    print("Your BMI is {}, you are clinically obese.".format(bmi))
