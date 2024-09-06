
import sys
import csv
from tabulate import tabulate


try:
    if len(sys.argv) == 3:
        in_file = sys.argv[1]
        out_file = sys.argv[2]

        stulist = []
        
        with open(in_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                stulist.append({"name": row["name"], "house": row["house"]})

        newstulist = []

        for student in stulist:
            name_parts = student['name'].split(',')
            last, first = name_parts
            first = first.strip()
            last = last.strip()

            newstulist.append({"first":first, "last": last, "house": student["house"]})

        def get_name(student_n):
            return student_n["name"]


        with open(out_file, "w") as file2:
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            for student_n in sorted(newstulist, key=lambda student_n: student_n["first"]):
                writer.writerow({"first": student_n["first"], "last": student_n["last"], "house": student_n["house"]})


    elif len(sys.argv) >= 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    else:
        sys.exit("Not a CSV file")
        
except FileNotFoundError:
    sys.exit("File does not exist")