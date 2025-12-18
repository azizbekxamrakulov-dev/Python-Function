def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To‘g‘ri topdingiz!")
    else:
        print("Xato, yana urinib ko‘ring")

sirli_son = 7   # oldindan belgilangan son
taxmin = int(input("Sonni taxmin qiling: "))

natija = check_guess(sirli_son, taxmin)
print_result(natija)