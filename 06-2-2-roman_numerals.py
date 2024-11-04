def roman_to_decimal(roman):
    def roman_char_to_value(char):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        return roman_values.get(char, 0)

    total = 0
    s = roman

    while s:
        if len(s) == 1 or roman_char_to_value(s[0]) >= roman_char_to_value(s[1]):
            total += roman_char_to_value(s[0])
            s = s[1:]
        else:
            difference = roman_char_to_value(s[1]) - roman_char_to_value(s[0])
            total += difference
            s = s[2:]

    return total
    

#example
roman_numeral = "MCMLXXVIII"
decimal_value = roman_to_decimal(roman_numeral)
print(f"The decimal value of {roman_numeral} is {decimal_value}")