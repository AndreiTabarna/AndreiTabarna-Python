import re

def extract_number(text):
    number = re.search(r'\d+', text)
    if number:
        return int(number.group())


text = input("Enter text: ")
print(f"Extracted number: {extract_number(text)}")
