#1----------------------------

def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]

print(fibonacci(10))


#2---------------------------

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(numbers):
    return [num for num in numbers if is_prime(num)]
    
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_primes(numbers))  


#3---------------------------

def set_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    diff_a_b = list(set(a) - set(b))
    diff_b_a = list(set(b) - set(a))
    return intersection, union, diff_a_b, diff_b_a
    
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(set_operations(a, b))



#4---------------------------

def compose(notes, moves, start_position):
    num_notes = len(notes)
    composed_song = []
    
    for move in moves:
        new_position = (start_position + move) % num_notes
        composed_song.append(notes[new_position])
        start_position = new_position
    
    return composed_song

    
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 1
print(compose(notes, moves, start_position))


#5---------------------------

def replace_below_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j] = 0
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(replace_below_diagonal(matrix))

#6--------------------------

from collections import Counter

def count_items(x, *lists):
    combined_list = [item for sublist in lists for item in sublist]
    counts = Counter(combined_list)
    result = [item for item, count in counts.items() if count == x]
    return result
    
lists = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]]
x = 2
print(count_items(x, *lists))
    
#7--------------------------

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def palindrome_numbers(numbers):
    palindromes = [num for num in numbers if is_palindrome(num)]
    max_palindrome = max(palindromes, default=None)
    return len(palindromes), max_palindrome

numbers1 = [121, 123, 1331, 454, 67876]
print(palindrome_numbers(numbers1)) 

#8--------------------------

def filter_characters(x, strings, flag=True):
    result = []
    for string in strings:
        if flag:
            filtered_chars = [char for char in string if ord(char) % x == 0]
        else:
            filtered_chars = [char for char in string if ord(char) % x != 0]
        result.append(filtered_chars)
    return result


x = 2
strings = ["test", "hello", "lab002"]
flag = False
print(filter_characters(x, strings, flag))

#9--------------------------

def find_obstructed_seats(matrix):
    obstructed_seats = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows-1):
        for j in range(cols):
            current_height = matrix[i][j]
            if matrix[i+1][j] < current_height:
                obstructed_seats.append((i+1, j))

    return obstructed_seats

stadium_matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

result = find_obstructed_seats(stadium_matrix)
print(result)

#10-------------------------

def merge_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    result = []
    for i in range(max_length):
        merged_tuple = tuple(lst[i] if i < len(lst) else None for lst in lists)
        result.append(merged_tuple)
    return result
    
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
print(merge_lists(list1, list2, list3))

#11-------------------------

def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1][2])
    
tuples = [('abc', 'bcd'), ('abc', 'zza')]
print(sort_tuples(tuples))
    
#12-------------------------

def group_by_rhyme(words):
    rhymes = {}
    for word in words:
        ending = word[-2:]
        if ending in rhymes:
            rhymes[ending].append(word)
        else:
            rhymes[ending] = [word]
    grouped_words = list(rhymes.values())
    return grouped_words
    
words = ['ana', 'banana', 'carte', 'arme', 'parte']
print(group_by_rhyme(words))


