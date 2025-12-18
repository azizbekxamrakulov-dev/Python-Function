# BMI hisoblash (butun sonlar bilan)
def calculate_bmi(weight, height):
    return weight // (height * height)  # butun son bilan

# BMI holati
def bmi_status(bmi):
    if bmi < 18:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Misol
weight = int(input("Og'irlik (kg): "))
height = int(input("Bo'y (m): "))

bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi}, Holati: {bmi_status(bmi)}")