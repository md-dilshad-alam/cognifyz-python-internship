def is_valid_email(email):
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False


email = input("Enter your email: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")