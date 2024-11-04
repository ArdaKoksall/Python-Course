def calculate_financial_aid(annual_income, num_children):
    if 30000 <= annual_income <= 40000 and num_children >= 3:
        return 1000 * num_children
    elif 20000 <= annual_income <= 30000 and num_children >= 2:
        return 1500 * num_children
    elif annual_income < 20000:
        return 2000 * num_children
    else:
        return 0

def main():
    while True:
        annual_income = float(input("Enter the family's annual income (or -1 to quit): "))
        if annual_income == -1:
            break
        num_children = int(input("Enter the number of children: "))
        aid_amount = calculate_financial_aid(annual_income, num_children)
        print(f"The financial aid allocated to the family is: ${aid_amount}")

if __name__ == "__main__":
    main()