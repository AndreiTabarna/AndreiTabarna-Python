string = input("Enter a string: ")
vowels_count = sum(1 for char in string if char.lower() in 'aeiou')
print(f"Number of vowels in the string: {vowels_count}")

