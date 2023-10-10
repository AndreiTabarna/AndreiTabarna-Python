def is_palindrome(number):
    return str(number) == str(number)[::-1]


num = int(input("Enter a number: "))
print(f"Is palindrome: {is_palindrome(num)}")
