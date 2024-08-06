
#decimal point
#x = float(input ("Whats x? "))
#y = float(input ("Whats y? "))

#z = x / y

#print (f"{z:.2f}")

def main():
    x = float(input ("Whats x? "))
    print("x squared is", square(x))

def square(n):
    return n * n    #(f"{n*n:.0f}")

if __name__ == "__main__":
    main()
