def isprime(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    n = int(input("Enter a number: "))
    for i in range(2, n + 1):
        while n % i == 0 and isprime(i):
            print(i)
            n //= i

main()