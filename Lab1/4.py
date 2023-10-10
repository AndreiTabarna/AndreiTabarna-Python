import re

input_string = input("Enter UpperCamelCase string: ")
snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', input_string).lower()
print(f"Converted string: {snake_case}")
