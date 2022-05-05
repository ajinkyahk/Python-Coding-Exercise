#Exercise - Prime Numbers

#Write your code below this line 👇
def prime_checker(number):
    if number%2==0:
        return print("It's not a prime number.")
    else: 
        count=number-2
    while(count>1):
        if number%(count)==0:
            return print("It's not a prime number.")
            
        else:
            count-=2
    print("It's a prime number.")
            




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
