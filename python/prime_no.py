'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input( "Enter till what number you want to check for prime numbers: "))
for i in range(2,n+1):
    if(is_prime(i)):
        print(i, end = " ")
''' 

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)

# n = int(input("Enter a number to find its factorial: "))
# print(f"The factorial of {n} is {fact(n)}")



# n = int(input("Enter a number to find its factorial: "))
# fact = 1 
# for i in range(1, n+1):
#     fact *= i
# print(f"The factorial of {n} is {fact}")
   
def armstring(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == n

n = int(input("Enter  a number to verify if it is an armstrong number: "))
print(f"{n} is an armstrong number" if armstring(n) else f"{n} is not an armstrong number")


