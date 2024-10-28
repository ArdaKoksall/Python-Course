
user_input = int(input("Please enter an integer: "))


for num in range(2, user_input + 1):
    is_prime = True

    # Check if the number is prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False  # The number is not prime
            break

    # If the number is prime, print it
    if is_prime:
        print(num)
