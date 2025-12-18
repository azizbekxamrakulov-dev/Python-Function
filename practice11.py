def calculate_tax(salary):
    if salary > 5_000_000:
        tax = salary * 0.20
    else:
        tax = salary * 0.13
    return tax

def calculate_net_salary(salary):
    return salary - calculate_tax(salary)

# Misol ishlatish
salary = float(input("Maoshingizni kiriting: "))
print(f"Soliq: {calculate_tax(salary)}")
print(f"Sof maosh: {calculate_net_salary(salary)}")