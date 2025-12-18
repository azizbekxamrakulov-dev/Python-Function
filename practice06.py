def is_valid_phone_number(phone):
    return phone.isdigit() and len(phone) == 9

telefon = input("Telefon raqamni kiriting: ")
print(is_valid_phone_number(telefon))