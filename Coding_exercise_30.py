password=input("Enter a new password:")
if len(password) < 7:
    print("Your password is weak.")
elif len(password)  >7:
    print("Great password there")
elif len(password)  == 7:
    print("Password is OK, but not too strong")