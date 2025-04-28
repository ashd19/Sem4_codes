
person1 = {"name": "X", "age": 20, "city": "Bengaluru"}


L1 = [1, 2, 3, 4, 5, 6, 7]


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def armstrong(a):
    temp = a
    sum = 0
    while a != 0:
        d = a % 10
        sum += d ** 3 
        a = a // 10

    if sum == temp:
        print(temp, "is an Armstrong number")
    else:
        print(temp, "is not an Armstrong number")
