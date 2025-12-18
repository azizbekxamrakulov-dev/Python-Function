# Palindrome tekshirish
def is_palindrome(text: str) -> bool:
    return text == text[::-1]

# Misol
word = input("So'zni kiriting: ")
if is_palindrome(word):
    print(" Palindrome")
else:
    print(" Palindrome emas")