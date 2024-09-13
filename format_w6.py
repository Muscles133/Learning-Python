import re

name = input ("Whats your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"hello, {name}")


#matches = re.search(r"^(.+), *(.+)$", name)

# if matches:
#     # last, first = matches.groups()
#     # name = f"{first} {last}"
#     last = matches.group(1)
#     first = matches.group(2)  # or name = matches.group(2) + " " + matches.group(1)
#     name = f"{first} {last}"
# print(f"hello, {name}")



if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
    
print(f"Hello, {name}")