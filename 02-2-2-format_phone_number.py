def format_phone_number(phone_number):
    if len(phone_number) != 10 or not phone_number.isdigit():
        raise ValueError("Phone number must be a 10-digit string.")
    
    area_code = phone_number[:3]
    first_part = phone_number[3:6]
    second_part = phone_number[6:]
    
    formatted_number = f"({area_code}) {first_part}-{second_part}"
    return formatted_number

# Example usage
phone_number = "4155551212"
formatted_number = format_phone_number(phone_number)
print(formatted_number)