import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Only accepts integers")
    sys.exit(1)
try:
    result = x/y
except ZeroDivisionError:
    print("Can not divide by 0")
    sys.exit(1)
print(f"result of x / y = {result}")