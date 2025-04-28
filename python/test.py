# gcd and lcm = a*b / gcd(a,b)
a = int(input("Enter an integer number: "))
b = int(input("Enter another integer number: "))

for i in range(max(a,b),0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        break


    