#Exercise - FizzBuzz

#Write your code below this row 👇
l1=list(range(1,101))
for i in l1:
    if i%3==0 and i%5!=0:
        print('Fizz')
    elif i%5==0 and i%3!=0:
        print('Buzz')
    elif i%5==0 and i%3==0:
        print('FizzBuzz')
    else:
        print(i)
