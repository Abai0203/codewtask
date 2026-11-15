# 1 

def sum_array(a):
    return sum(a)

# 2

def digitize(n):
    return [int(c) for c in reversed(str(n))]

# 3

def summation(num):
    return num * (num + 1) // 2

# 4

def factorial(n):
    import math

    return math.factorial(n)

# 5 

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# 6

def remove_char(s):
    return s[1:-1]

# 7

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 8

def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)

# 9

def dna_to_rna(dna):
    return dna.replace('T', 'U')

# 10

def greet(name):
    return f"Hello, {name} how are you doing today?"

# 11

def find_deleted_number(arr, mixed_arr):
    return sum(arr) - sum(mixed_arr)

# 12

def positive_to_negative(binary):
    flipped = [1 - b for b in binary]
    carry = 1
    result = [0] * len(binary)
    for i in range(len(binary) - 1, -1, -1):
        s = flipped[i] + carry
        result[i] = s % 2
        carry = s // 2
    return result

# 13

def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


# 14

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)