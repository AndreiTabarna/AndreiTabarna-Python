import re
from collections import Counter

def most_common_letter(text):
    letters = re.findall(r'[a-zA-Z]', text)
    letter_counts = Counter(letters)
    most_common = letter_counts.most_common(1)[0]
    return most_common

text = input("Enter a string: ")
letter, count = most_common_letter(text)
print(f"Most common letter: {letter} ({count} times)")

