def describe_wavelength(wavelength):
    if wavelength > 1e-1 and wavelength < 3e9:
        return "Radio Wave"
    elif 1e-3 <= wavelength <= 1e-1 or 3e9 <= wavelength <= 3e11:
        return "Microwave"
    elif 7e-7 <= wavelength < 1e-3 or 3e11 <= wavelength < 4e14:
        return "Infrared"
    elif 4e-7 <= wavelength < 7e-7 or 4e14 <= wavelength < 7.5e14:
        return "Visible light"
    elif 1e-8 <= wavelength < 4e-7 or 7.5e14 <= wavelength < 3e16:
        return "Ultraviolet"
    elif 1e-11 <= wavelength < 1e-8 or 3e16 <= wavelength < 3e19:
        return "X-rays"
    elif wavelength < 1e-11 or wavelength > 3e19:
        return "Gamma rays"
    else:
        return "Unknown spectrum"

def main():
    try:
        wavelength = float(input("Enter the wavelength value (in meters): "))
        description = describe_wavelength(wavelength)
        print(f"The wavelength corresponds to: {description}")
    except ValueError:
        print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    main()