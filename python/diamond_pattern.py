#diamond pattern using nested loops 
n = int(input("Enter the number of rows for the diamond pattern: "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))    
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


    # area of etc etc 