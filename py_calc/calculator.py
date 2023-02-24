#!/usr/bin/python3
##
###

def add(x, y):
    return x+y

    
def substruct(x, y):
    return x-y


def multiply(x, y):
    return x*y


def devide(x, y):
    if str(x/y)[2] == 0:
         return str(x/y)[2]
    else:
        return x/y


def square(x, y):
    return x ** y



print("!*!*!*   X & Y must be integers numbers :   ")
# take user input & store it in variables
X = int(input("Enter X= "))
Y = int(input("Enter Y= "))


# print results to the console
print("\n****\t\tcommon operations are: \t\t****\n")
print("1- Addition: \t\t", add(X,Y))
print("2- Substraction: \t", substruct(X,Y))
print("3- Multiplication: \t", multiply(X,Y))
print("4- Devision: \t\t", devide(X,Y))
print("4- Square: \t\t", square(X,Y))
 



















