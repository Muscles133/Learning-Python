
import re

email = input("Whats your email? ").strip()

# if "@" in email:
#     print("Valid")
# else:
#     print("Invalid")


# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("Invalid")


# if re.search("@", email):
#     print("valid")

# else:
#     print("Invalid")

#re.search(pattern, string, flags=0)


if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):   # \w = [a-zA-Z0-9_]
    print("valid")

else:
    print("Invalid")


