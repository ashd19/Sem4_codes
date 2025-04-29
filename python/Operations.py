# a pacakage is a folder that contains a special file called __init__.py 
# and modules / files 

def add(x, y):
    """This function adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers and returns the result."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers and returns the result."""
    return x * y
def divide(x, y):   
    """This function divides two numbers and returns the result."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
def modulus(x, y):
    """This function returns the modulus of two numbers."""
    return x % y
def power(x, y):
    """This function returns the power of two numbers."""
    return x ** y

def armstrong_number(num):
    """This function checks if a number is an Armstrong number."""
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

def prime_number(num):
    """This function checks if a number is prime."""
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False 
    

for i in range(1,100):
    if prime_number(i):
        print(f"{i} ")
    else:
        continue