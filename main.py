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

# 15

def string_to_number(s):
    return int(s)

# 16

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

# 17

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# 18

def friend(x):
    return [name for name in x if len(name) == 4]

# 19

def smash(words):
    return " ".join(words)


# 20

def high_and_low(numbers):
    nums = [int(x) for x in numbers.split()]
    return f"{max(nums)} {min(nums)}"


# 21

def filter_string(st):
    return int("".join(c for c in st if c.isdigit()))

# 22

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0