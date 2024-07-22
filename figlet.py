from pyfiglet import Figlet
import random
import sys

# figlet = Figlet()
# figlet.getFonts()
# figlet.setFont(font=f)
# print(figlet.renderText(s))


if len(sys.argv) == 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many arguments")

elif len(sys.argv) == 3:
    figlet = Figlet()
    fonts = figlet.getFonts()
    font_call = sys.argv[1]
    font_arg = sys.argv[2]
    accept_f = ["-f", "--font"]

    if font_call not in accept_f:
        print(f"Error: '{font_call}' is not a valid input.")
        sys.exit(f"Valid inputs are: {', '.join(accept_f)}")
        # sys.exit(1)

    elif font_arg not in fonts:
        print(f"Error: '{font_arg}' is not a valid input.")
        sys.exit(f"Valid inputs are: {', '.join(fonts)}")
        # sys.exit(1)

    else:
        text = input("Input: ")
        figlet.setFont(font=font_arg)
        sys.exit(figlet.renderText(text))

else:
    text = input("Input: ")
    figlet = Figlet()
    fonts = figlet.getFonts()
    list_len = len(fonts)
    ran_n = random.randint(1, list_len)
    ran_f = fonts[ran_n]
    figlet.setFont(font=ran_f)
    print(figlet.renderText(text))

    # print(fonts)

    # try:
    #     print("hello, my name is", sys.argv[1])
    # except IndexError:
    #     print("Too few arguments")

    # text = input("Input: ")
    # figlet.setFont(font='stampatello')
    # print(figlet.renderText(text))


# main()
