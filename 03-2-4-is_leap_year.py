def is_leap_year(year):
    if year > 1582 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        return True
    return False

def main():
    year = int(input("Enter a year greater than 1582: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()