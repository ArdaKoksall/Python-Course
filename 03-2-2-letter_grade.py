# Prompt the user to enter a letter grade
letter_grade = input("Enter a letter grade: ").strip().upper()

# Ensure the input is either a single character or a valid letter-modifier combination
if len(letter_grade) == 1 and letter_grade.isalpha():
    # Get the numeric value for the single letter grade
    if letter_grade == 'A':
        numeric_grade = 4.0
    elif letter_grade == 'B':
        numeric_grade = 3.0
    elif letter_grade == 'C':
        numeric_grade = 2.0
    elif letter_grade == 'D':
        numeric_grade = 1.0
    elif letter_grade == 'F':
        numeric_grade = 0.0
    else:
        numeric_grade = "Invalid grade"
elif len(letter_grade) == 2 and letter_grade[0].isalpha() and letter_grade[1] in ['+', '-']:
    # Extract the base letter and the modifier (+ or -)
    base = letter_grade[0]
    modifier = letter_grade[1]

    # Validate the base letter and ensure it is not 'F' with a modifier
    if base == 'F':
        numeric_grade = "Invalid grade"
    else:
        # Get the numeric value for the base letter
        if base == 'A':
            numeric_grade = 4.0
        elif base == 'B':
            numeric_grade = 3.0
        elif base == 'C':
            numeric_grade = 2.0
        elif base == 'D':
            numeric_grade = 1.0
        else:
            numeric_grade = "Invalid grade"

        # Adjust the numeric value based on the modifier
        if numeric_grade != "Invalid grade":
            if modifier == '+':
                if base != 'A':  # A+ remains 4.0
                    numeric_grade += 0.3
            elif modifier == '-':
                numeric_grade -= 0.3
else:
    # Handle cases where the input has more than two characters or invalid input
    numeric_grade = "Invalid grade"

# Print the numeric value of the entered letter grade
print(f"The numeric value of grade {letter_grade} is {numeric_grade}")