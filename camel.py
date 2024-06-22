def main():
    camelcase = "ThisIsACamelString" #input("Convert camelCase to snake_case: ")
    Snake_Convert(camelcase)


def Snake_Convert(camelcase):
    for letters in camelcase:
            if letters.islower():
                 print(letters, end='')
            else:
                 letters.lower()
                 print(f"_ {letters}", end='')
            
            


main()