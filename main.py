#Write a function that takes a string as input and returns the reversed string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

#Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
def count_vowels(s):
    vowels = set('aeiou')
    return sum(1 for char in s.lower() if char in vowels)

print(count_vowels("Hello World"))


#Write a function that takes a non-negative integer and returns the sum of its digits.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(5678))  # Output: 26