
# def main():
#     plate = "CX111K"

#     for chars in plate:
#         if not chars.isdigit():
#             continue
#         else:
#             print (chars, end='')

# main()


# start with 2 letters


# Max 6 characters min 2 characters


# if there are numbers no alpha after.


# first number cannot be 0


# only alpha and ints



def main():
    plate = "CS50" #input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if Starts_with_two_alpha(s):
        if six_max_two_min(s):
            if No_alph_after_num(s):
                if Only_num_alph(s):
                    if First_Num_0(s):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def Starts_with_two_alpha(s):
    if s[:2].isalpha():
        return True
    else:
        return False

def six_max_two_min(s):
    len_plate = len(s)
    if 2<= len_plate <= 6:
        return True
    else:
        return False

def No_alph_after_num(s):
    if s[-1].isalpha() and s[-2].isdigit():
        return False
    else:
        return True

def Only_num_alph(s):
    for char in s:
        if char.isalpha() or char.isdigit():
            return True
        else:
            return False

def First_Num_0(s):
    int_count = 0
    for p in s:
        if p.isdigit():
            int_count += 1
            if int_count == 1 and p == '0':
                return False
            else:
                return True
        else:
            return True  

main()



# def No_alph_after_num(s):
#     found_num = False
#     for char in s:
#         if char.isdigit():
#             found_num = True
#         elif found_num and char.isalpha():
#             return False
#     return True


# def First_Num_0(s):
#     for char in s:
#         if char.isdigit():
#             return char != '0'
#     return True