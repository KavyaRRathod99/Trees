#def in the calculator
def add(a , b):
    return a + b
def sub(a , b):
    return a - b
def divied(a , b):
    return a// b
def multiply(a , b):
    return a*b

#then using the above value to store all operators and then use that file 
  and modules 
#1. using all the function
from Calculator import* 
a=9
b=8
print(add(a,b))
print(sub(a,b))
print(multiply(a,b))
print(divied(a,b))

# 2. using import calculator to access calculator
import Calculator
a=9
b=8
print(Calculator.add(a,b))
print(Calculator.sub(a,b))
print(Calculator.multiply(a,b))
print(Calculator.divied(a,b))

  #3. from the calcultor i want to import add and multiply function

  from calculator import multiply,add
a=9
b=8
print(multiply(a,b))
print(add(a,b))

  
