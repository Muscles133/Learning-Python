def main():
    word = input("I will twitify your input: ")
    result = shorten(word)
    print(result)



def shorten(word):
    vowels = {"a", "e", "i", "o", "u"} #break uppercase {"A", "E", "I", "O", "U"}
    return ''.join(letter for letter in word if letter not in vowels)

    
    # for letter in word:
    #     if letter not in vowels:
    #         return ''.join


if __name__ == "__main__":
    main()