import math

numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
gcd = math.gcd(*numbers)
print(f"The greatest common divisor is: {gcd}")
