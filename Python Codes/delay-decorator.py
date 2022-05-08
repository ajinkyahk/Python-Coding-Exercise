import time

def delay_decorator(function):
  def wrapper():
    time.sleep(2)
    function()
  return wrapper

@delay_decorator
def say_hello():
  print("hello")
  
@delay_decorator
def say_bye():
  print("bye!!")
  
def say_greeting():
  print("How are you?")
  
  

say_hello()
say_bye()

decorated_function = delay_decorator(say_greeting)
decorated_function() 
