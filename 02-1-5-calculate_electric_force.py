def calculate_electric_force(Q1, Q2, r):
    epsilon_0 = 8.854e-12  # Farad/meter
    k = 1 / (4 * 3.141592653589793 * epsilon_0)
    force = k * (Q1 * Q2) / (r ** 2)
    return force

def main():
    try:
        Q1 = float(input("Enter the charge Q1 (in Coulombs): "))
        Q2 = float(input("Enter the charge Q2 (in Coulombs): "))
        r = float(input("Enter the distance r (in meters): "))
        
        if r <= 0:
            print("Distance r must be greater than zero.")
            return
        
        force = calculate_electric_force(Q1, Q2, r)
        print(f"The electric force between the particles is: {force} N")
    except ValueError:
        print("Please enter valid numerical values for Q1, Q2, and r.")

if __name__ == "__main__":
    main()