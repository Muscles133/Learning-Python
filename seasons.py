from datetime import date, timedelta
import re
import sys
import inflect

p = inflect.engine()


def main():
    try:
        mins = get_mins(input("Date of Birth: "))
        words = min_to_word(mins)
        print(words)

        t = 127
        print(min_to_word(t))

    except ValueError:
        sys.exit("Invalid date")



def get_mins(m):
    try:
        birth = date.fromisoformat(m)
        today = date.today()
        timedelta = today - birth
        secs = timedelta.total_seconds()
        mins = int(secs / 60)
        return mins

    except ValueError:
        raise ValueError("Invalid date")


def min_to_word(mins):
    try:
        num = int(mins)

        num2 = p.number_to_words(num, andword="")

        return f"{num2} minutes"

    except ValueError:
        raise ValueError("Invalid Number")


if __name__ == "__main__":
    main()
