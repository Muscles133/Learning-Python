cal = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

def main():

    while True:
        try:
            outdate = input("Date: ")
            outdate_c = process_input(outdate)
            a,b,c = outdate_c.split("/")
            day = int(b)
            month = con_month(a)
            year = int(c)

            if 1 <= day <= 31:
                print (f"{year}-{month:02}-{day:02}")
                break

            else:
                ValueError
    
        except KeyError:
            pass
        except EOFError:
            break
        except ValueError:
            pass

def con_month(a):
    if a.isdigit():
        return int(a)
    else:
        result = int(cal.index(a)+1)
        return result
    
def process_input(i):
    rpl = i.replace(' ', '/').replace(',', '')
    return rpl

main()