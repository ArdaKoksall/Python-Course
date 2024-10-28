input_string = input("Enter a string: ")

# I. Only the uppercase letters of the string
# I. Only the uppercase letters of the string
uppercase_letters = ""
for char in input_string:
    if char.isupper():
        uppercase_letters += char

# II. Letters in even positions in the string
even_position_letters = ""
for i in range(len(input_string)):
    if i % 2 == 0:
        even_position_letters += input_string[i]

# III. The same string in which, instead of vowels (upper or lowercase), there is an underscore (_)
vowels = "AEIOUaeiou"
replaced_vowels_string = ""
for char in input_string:
    if char in vowels:
        replaced_vowels_string += "_"
    else:
        replaced_vowels_string += char

# IV. The number of numeric digits in the string
numeric_digits_count = 0
for char in input_string:
    if char.isdigit():
        numeric_digits_count += 1

# V. The positions of all vowels in the string
vowel_positions = []
for i, char in enumerate(input_string):
    if char in vowels:
        vowel_positions.append(i)

# Display results
print("I. Uppercase letters:", uppercase_letters)
print("II. Letters in even positions:", even_position_letters)
print("III. String with vowels replaced by underscores:", replaced_vowels_string)
print("IV. Number of numeric digits:", numeric_digits_count)
print("V. Positions of all vowels:", vowel_positions)
