def count_ones_bits(number):
    return bin(number).count('1')


num = int(input("Enter a number: "))
print(f"Number of bits with value 1: {count_ones_bits(num)}")

