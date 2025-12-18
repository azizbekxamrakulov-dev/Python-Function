def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    if age >= 18:
        print("Balog‘atga yetgansiz")
    else:
        print("Balog‘atga yetmagansiz")

tugilgan = int(input("Tug‘ilgan yilni kiriting: "))
hozirgi = int(input("Hozirgi yilni kiriting: "))

calculate_age(tugilgan, hozirgi)