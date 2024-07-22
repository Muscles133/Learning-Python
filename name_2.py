import sys

#command line argument sys.argv = agrument vector
if len(sys.argv) <2:
    sys.exit("Too few arguments")
elif len(sys.argv) >2:
    sys.exit("Too many arguments")

print("hello, my name is",sys.argv[1]) # system 0 is the file name

# except IndexError:
#     print('Too few arguments')

# index error if its outside of the list

 