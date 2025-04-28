try:
    print("Enter temperature to convert from: 1. Fahrenheit, 2. Kelvin, 3. Celsius")
    i = int(input("From (1/2/3): "))
    
    print("Enter temperature to convert to: 1. Fahrenheit, 2. Kelvin, 3. Celsius")
    f = int(input("To (1/2/3): "))
    
    a = float(input("Enter temperature value: "))
    
    if i == 1:  # From Fahrenheit
        if f == 1:
            print(a)
        elif f == 2:
            r = ((a - 32) * (5/9)) + 273.15
            print(r)
        elif f == 3:
            r = (a - 32) * (5/9)
            print(r)
        else:
            print("Invalid target unit.")
    
    elif i == 2:  # From Kelvin
        if f == 1:
            r = (a - 273.15) * (9/5) + 32
            print(r)
        elif f == 2:
            print(a)
        elif f == 3:
            r = a - 273.15
            print(r)
        else:
            print("Invalid target unit.")
    
    elif i == 3:  # From Celsius
        if f == 1:
            r = (a * (9/5)) + 32
            print(r)
        elif f == 2:
            r = a + 273.15
            print(r)
        elif f == 3:
            print(a)
        else:
            print("Invalid target unit.")
    
    else:
        print("Invalid source unit.")
        
except Exception as e:
    print("Error:", e)
