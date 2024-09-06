import sys

try:
    if len(sys.argv) == 2:
        for arg in sys.argv[1:]:

            with open(arg, "r") as file:
                content = file.read()
                lines = content.split('\n')
                non_empty_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
                count = len(non_empty_lines)
                print(count)

    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    else:
        sys.exit("Not a Python file")
        
except FileNotFoundError:
    sys.exit("File does not exist")


