# Parol kuchini tekshirish
def is_strong_password(password: str) -> bool:
    return len(password) >= 8

# Misollar
pwd = input("Parolni kiriting: ")
if is_strong_password(pwd):
    print(" Kuchli parol")
else:
    print(" Kuchsiz parol")