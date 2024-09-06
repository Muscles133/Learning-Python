from tabulate import tabulate
import sys
import csv


try:
    if len(sys.argv) == 2:
        for arg in sys.argv[1:]:

            with open(arg, "r") as file:
                menu = csv.DictReader(file)
                print(tabulate(menu, headers="keys", tablefmt="grid"))


    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    else:
        sys.exit("Not a CSV file")
        
except FileNotFoundError:
    sys.exit("File does not exist")