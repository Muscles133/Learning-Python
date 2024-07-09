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

# path 1: September 8, 1636
# path 2: 9/8/1636

def main():

    while True:
        try:
            outdate = input("Date: ").strip()
            if outdate.startswith(tuple(cal)):
                a,b,c = outdate.split(" ")
                if b.endswith(","):
                    b2 = b.replace(',', '') # cant int string the replace shit.
                    b3 = int(b2)
                    day = ck_day(b3)
                    month = con_month(a)
                    year = int(c)
                    print (f"{year}-{month:02}-{day:02}")
                    break
                else:
                    ValueError

            else:
                a,b,c = outdate.split("/")
                day = ck_day(int(b))
                month = ck_month(int(a))
                year = int(c)
                print (f"{year}-{month:02}-{day:02}")
                break

        except KeyError:
            pass
        except TypeError:
            pass
        except EOFError:
            break
        except ValueError:
            pass

def con_month(a):
    result = int(cal.index(a)+1)
    return result

def ck_month(m):
    if 1 <= m <= 12:
        return m
    else:
        pass
    
def ck_day(b):
    if 1 <= b <= 31:
        return b
    else:
        pass

    
# def process_input(i):
#     rpl = i.replace(' ', '/').replace(',', '')
#     return rpl

"""
i had a better verion of this code but it didnt pass the tests becuase it processed the values better rather than accepting
perfect input

"""

main()