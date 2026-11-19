# Q1: Username Validation System

# Accept the username from the user
username = input("Enter a username: ")

# Rules:
# 1. Must not be only spaces (strip() removes spaces at both ends)
# 2. Must not be "admin" in any combination of upper/lower case
# 3. Must have at least 5 characters
# The spaces-only check comes first so " " gets the most accurate reason.
if username.strip() == "":
    print("Invalid username: it cannot contain only spaces.")
elif username.lower() == "admin":
    print("Invalid username: 'admin' is not allowed (case is ignored).")
elif len(username) < 5:
    print("Invalid username: it must contain at least 5 characters.")
else:
    print("Valid username.")
