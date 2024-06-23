
def main():
    plate = "CX111K"

    for chars in plate:
        if not chars.isdigit():
            continue
        else:
            print (chars, end='')

main()