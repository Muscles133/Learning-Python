def main():
    statement = input("I will twitify your input: ")
    remove_vowels(statement)

def remove_vowels(statement):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for letter in statement:
        if letter not in vowels:
            print(letter, end='')
    
main()