#diamond pattern using nested loops 
n = int(input("Enter the number of rows for the diamond pattern: "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))    
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


    # area  of cylinger = 2 * pi * r * h + 2 * pi * r^2
# volume of cylinger = pi * r^2 * h
# volume of sphere = (4/3) * pi * r^3
# volume of cone = (1/3) * pi * r^2 * h
# volume of cube = a^3
# volume of cuboid = l * b * h
# volume of pyramid = (1/3) * l * b * h
# volume of prism = base area * height