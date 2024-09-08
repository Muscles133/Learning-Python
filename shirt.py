
import sys
import csv
from PIL import Image

try:
    if len(sys.argv) == 3:
        in_file = "before1.jpg" #sys.argv[1]
        out_file = "after1.jpg" #sys.argv[2]



       





    elif len(sys.argv) >= 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    else:
        sys.exit("Not a JPG file")
        
except FileNotFoundError:
    sys.exit("File does not exist")