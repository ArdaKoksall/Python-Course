def display_string_summary(s):
    if len(s) < 6:
        print("The string must be more than 6 characters long.")
    else:
        result = s[:3] + "..." + s[-3:]
        print(result)


string = "PYTHON IS EASY I WANT TO USE C"
display_string_summary(string)