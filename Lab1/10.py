def count_words(text):
    words = text.split()
    return len(words)


text = input("Enter a text: ")
print(f"Number of words: {count_words(text)}")

