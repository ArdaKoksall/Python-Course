def random_number_generator(seed, a=32310901, b=1729, m=2**24, count=100):
    random_numbers = []
    x_prev = seed
    for _ in range(count):
        x_next = (a * x_prev + b) % m
        random_numbers.append(x_next)
        x_prev = x_next
    return random_numbers

def main():
    seed = int(input("Enter the initial seed value: "))
    random_numbers = random_number_generator(seed)
    for i, num in enumerate(random_numbers, start=1):
        print(f"{i}: {num}")

main()