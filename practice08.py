# Celsius → Fahrenheit
def c_to_f(c):
    return c * 9/5 + 32

# Fahrenheit → Celsius
def f_to_c(f):
    return (f - 32) * 5/9

# Misollar
print("25°C →", c_to_f(25), "°F")
print("77°F →", f_to_c(77), "°C")