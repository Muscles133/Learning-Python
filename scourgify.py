import sys
import csv


def main():
    check_agr()

    try:
        in_file = sys.argv[1]
        out_file = sys.argv[2]

        with open(in_file, "r") as file:
            reader = csv.DictReader(file)
            with open(out_file, "w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(",")
                    house = row["house"]
                    writer.writerow(
                        {"first": first.strip(), "last": last.strip(), "house": house}
                    )

    except:
        sys.exit("Failed to read and write")


def check_agr():
    try:
        if len(sys.argv) == 3:
            return
        elif len(sys.argv) >= 2:
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        else:
            sys.exit("Not a CSV file")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
