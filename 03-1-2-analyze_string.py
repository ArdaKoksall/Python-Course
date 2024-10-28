def analyze_string(s):
    if s.isalpha():
        print("The string contains only letters.")
    if s.isupper():
        print("The string contains only capital letters.")
    if s.islower():
        print("The string contains only lowercase letters.")
    if s.isdigit():
        print("The string contains only decimal numeric digits.")
    if s.isalnum():
        print("The string contains only letters and digits.")
    if s and s[0].isupper():
        print("The string starts with a capital letter.")
    if s.endswith('.'):
        print("The string ends with a point.")

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    analyze_string(user_input)