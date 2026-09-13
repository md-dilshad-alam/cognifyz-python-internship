def is_palindrome(text):
    return text == text[::-1]


user_input = input("Enter a word: ")

if is_palindrome(user_input):
    print("It is a palindrome")
else:
    print("It is not a palindrome")