import random
import sys


def main():
    while True:
        try:
            level = int(input("level: "))  # prompts for number

            if level >= 1:
                print(f"Level {level}")
                correct_guess = random.randint(1, level)

                while True:
                    try:
                        guess = int(input("guess: "))
                        if guess >= 1:
                            # print(guess)
                            if guess > correct_guess:
                                print("too high")
                            elif guess < correct_guess:
                                print("Too Low")
                            else:
                                sys.exit(f"Correct Guess!")

                    except EOFError:
                        # result = p.join(names)
                        sys.exit(f"Exit")
                        

                    except KeyError:
                        pass

                    except ValueError:
                        pass

        except EOFError:
            # result = p.join(names)
            sys.exit(f"Exit")

        except KeyError:
            pass

        except ValueError:
            pass


main()
