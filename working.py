import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
        #hours = "12:00 AM to 12:00 PM"
        #print(convert(hours))

    except ValueError:
        sys.exit(f"ValueError")


def convert(s):
    ap = "AM|PM"  # either or
    t = "1[0-2]:[0-5][0-9]|[0-9]:[0-5][0-9]|1[0-2]|[1-9]"  # this is the re for the time part

    def pro(start, start_status):  # process the start or the finish
        if start_status == "AM":
            if len(start) >= 3:
                starta, startb = start.split(":")
                starta = int(starta)

                if startb != "00":
                    startb = int(startb)
                else:
                    pass

                if starta <= 11:
                    start24 = f"{starta:02}:{startb:2}"
                else:
                    start24 = f"00:{startb:2}"
            else:
                if int(start) <= 11:
                    start24 = int(start)
                    start24 = f"{start24:02}:00"
                else:
                    start24 = "00:00"

        if start_status == "PM":
            if len(start) <= 2:
                if int(start) <= 11:
                    startpro = int(start) + 12
                    start24 = f"{startpro}:00"
                else:
                    start24 = "12:00"

            else:
                starta, startb = start.split(":")
                starta = int(starta)
                if startb != "00":
                    startb = int(startb)
                else:
                    pass

                if int(starta) <= 11:
                    startpro = int(starta) + 12
                    start24 = f"{startpro}:{startb}"
                else:
                    start24 = f"12:{startb}"

        return start24

    try:
        if matches := re.search(
            rf"^({t}) ({ap}) to ({t}) ({ap})$", s
        ):  # split the work into 4 parts
            start = matches.group(1)
            start_status = matches.group(2)
            finish = matches.group(3)
            finish_status = matches.group(4)

            start_result = pro(start, start_status)
            finish_result = pro(finish, finish_status)

            return f"{start_result} to {finish_result}"

        else:
            raise ValueError("ValueError")

    except ValueError:
        raise ValueError("ValueError")


if __name__ == "__main__":
    main()
