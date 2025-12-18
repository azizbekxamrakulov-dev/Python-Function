def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

ball = int(input("Ball kiriting: "))
print("Baho:", get_grade(ball))