import re

password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password")

elif not re.search(r"[A-Z]", password):
    print("Weak password")

elif not re.search(r"[a-z]", password):
    print("Weak password")

elif not re.search(r"[0-9]", password):
    print("Weak password")

elif not re.search(r"[@$!%*?&]", password):
    print("Weak password")

else:
    print("Strong password")