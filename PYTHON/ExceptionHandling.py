try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    print("Choose Operation: 1. Add, 2. Subtract, 3. Multiply, 4. Divide")
    c = int(input("Enter choice (1/2/3/4): "))
    
    r = 0
    
    if c == 1:
        r = a + b
        print(r)
    elif c == 2:
        r = a - b
        print(r)
    elif c == 3:
        r = a * b
        print(r)
    elif c == 4:
        try:
            r = a / b
            print(r)
        except Exception as e:
            print("Error during division:", e)
    else:
        print("Choose a valid option")
        
except Exception as e:
    print("Invalid input:", e)
