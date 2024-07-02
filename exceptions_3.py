while True: 
    try:
        x = int(input("Give me x? "))
    
    except ValueError:
        print('x is not an integer')

    else:
        break

print(f"x is {x}")ca