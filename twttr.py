def main():
    word = input("I will twitify your input: ")
    print(shorten(word))



def shorten(word):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} #break uppercase {"A", "E", "I", "O", "U"}
    result = ''.join(letter for letter in word if letter not in vowels)
    return result


if __name__ == "__main__":
    main()
