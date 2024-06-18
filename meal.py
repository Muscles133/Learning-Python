def main():
    time = convert(input("What time is it? "))

    if  7 <= time < 8:
        print("Breakfast time")
    elif  12 <= time < 13:
        print("Lunch time")
    elif  18 <= time < 19:
        print("Dinner time")
    else:
        print("Unsure what time you are using")

def convert(time):
    
    if time.endswith("p.m."):
        hourmin, ampm = time.split()
        h, m = hourmin.split(":")
        return int(h) + int(m)/60 + 12
    
    elif time.endswith("a.m."):
        hourmin, ampm = time.split()
        h, m = hourmin.split(":")
        return int(h) + int(m)/60
    
    else: 
        h,m = time.split(":")
        return int(h) + int(m)/60

if __name__ == "__main__":
    main()