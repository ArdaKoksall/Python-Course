numbers = []
partial_sum = 0
even_count = 0
odd_count = 0

while True:
    user_input = input("Enter an integer (or press Enter to finish): ")
    if user_input == "":
        break

    number = int(user_input)

    numbers.append(number)
    partial_sum += number
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

        
print(f"Partial sum: {partial_sum}")
print(f"Minimum value: {min(numbers)}")
print(f"Maximum value: {max(numbers)}")
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")
