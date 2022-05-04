#Exercise - Dictionary Comprehension 2 

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
l1=sentence.split(' ')
# Write your code below:
result={x:len(x) for x in l1}


print(result)

