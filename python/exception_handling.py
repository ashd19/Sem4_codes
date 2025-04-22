try:
    print(x)
    
except NameError:
    print("x is not defined")

    # --------------------------------------------
try:
    print(12//0)
    
except NameError:
    print("x is not defined")
except ZeroDivisionError:
    print("Division by zero is not allowed")

# --------------------------------------------
# try:
#     n = int(input("Enter an integer number: "))
  
# except ValueError:
#     print("Invalid input: Please enter a valid integer.")

#---------------------------------------------
 
try:
    from math import srt
    
except ImportError:
    print("ImportError: The module or function could not be imported.")

    #---------------------------------------------

list = [1, 2, 3, 4, 5]
try:
    print(list[5])
except IndexError:
    print("IndexError: The 5th index is out of range.")
else:
    print("No error occurred.")
finally:
    print("Execution completed.")
#---------------------------------------------
from math import factorial
try:
        print(factorial(1000012123123213123132142341324))
except OverflowError:
    print("OverflowError: The number is too large to be represented.")

#syntax error
try:
    print(1 + 2)
except SyntaxError:
    print("SyntaxError: There is a syntax error in the code.")

#tab error
try:
    print(1 + 2)
except TabError:
    print("TabError: There is a tab error in the code.")


# try:
#   f = open("demofile.txt")
# try:
#     f.write("Lorum Ipsum")
# except:
#     print("Something went wrong when writing to the file")
# finally:
#     f.close()

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed") 