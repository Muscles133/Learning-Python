import random
import sys

def main():
    lvl = get_level()       # gets the correct level
    score = 0

    for _ in range(10):                 # populate games
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        result = x + y
        tries = 0
        while tries != 3:
            try:
                guess = int(input(f"{x}+{y}="))
                if guess == result:
                    tries = 0
                    score += 1
                    break
                else:
                     tries += 1

            except ValueError:
                tries += 1
                pass
            except EOFError:
                sys.exit(f"Exit")
        print(f"{x}+{y}={result}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if 1<= lvl <= 3:
                return lvl
            else:
                 pass
        except ValueError:
            pass
        except EOFError:
                        sys.exit(f"Exit")

def generate_integer(level):
    if level == 1:
         return random.randint(1,9)
    elif level == 2:
         return random.randint(10, 99)
    else:
         return random.randint(100, 999)
    
# def game():
#     x = generate_integer(lvl)
#     y = generate_integer(lvl)
#     while True:
#         try:
#             lvl = int(input("Level: "))
#             if 1<= lvl <= 3:
#                 return lvl
#             else:
#                  pass
#         except ValueError:
#             pass
#         except EOFError:
#                         sys.exit(f"Exit")

if __name__ == "__main__":
    main()


