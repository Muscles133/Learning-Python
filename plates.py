# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     platelength = len(s)  # tells me the length of the plate
#     if platelength >= 2 and platelength <= 6:  # lets the correct length pass through
#         if is_num_alph(s):  # filters out plates that do not contain numbers or letters
#             if first_2_letters(s):  # first 2 are letters
#                 if first_number_used(s):  # 0 can't be the first number
#                     if not alph_after_num(s):  # no letters after numbers
#                         return True
#                     else:
#                         return False
#                 else:
#                     return False
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
    
# def is_num_alph(s):        #figure out if its just numbers and letters
#     for character in s:
#         if not (character.isdigit() or character.isalpha()):
#             return False
#     return True
        
# def first_2_letters(s):     #first 2 are letters
#         if len(s) >= 2 and s[0].isalpha() and s[1].isalpha():
#             return True
#         return False
        
# """
# def first_number_used(s):  #work out if 0 is the first number
#     num = ""
#     num_found = False

#     for numbers in s:
#         if numbers.isdigit():
#             num += numbers
#             num_found = True
#         elif num_found:
#             break
#     if num:
#         return not num.startswith('0')
    
#     return True
# """

# def first_number_used(s):  #work out if 0 is the first number
#     num_found = False

#     for character in s:
#         if character.isdigit():
#             if num_found:
#                 if character == '0':
#                     return False
#                 else:
#                     return True
#             else:
#                 num_found = True
                
#     return True


# def alph_after_num(s):      #work out letter after number
#     for i in range(len(s) - 1):
#         if s[i].isdigit() and s[i + 1].isalpha():
#             return True
#     return False


# main()

# #vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    platelength = len(s)  # tells me the length of the plate
    if platelength >= 2 and platelength <= 6:  # lets the correct length pass through
        if is_num_alph(s):  # filters out plates that do not contain numbers or letters
            if first_2_letters(s):  # first 2 are letters
                if first_number_used(s):  # 0 can't be the first number
                    if not alph_after_num(s):  # no letters after numbers
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

def is_num_alph(s):  # figure out if it's just numbers and letters
    for character in s:
        if not (character.isdigit() or character.isalpha()):
            return False
    return True

def first_2_letters(s):  # first 2 are letters
    if len(s) >= 2 and s[0].isalpha() and s[1].isalpha():
        return True
    return False

def first_number_used(s):  # work out if 0 is the first number
    num = ""
    num_found = False

    for char in s:
        if char.isdigit():
            num += char
            num_found = True
        elif num_found:
            break

    if num:
        return not num.startswith('0')

    return True

def alph_after_num(s):  # work out if a letter follows a number
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return True
    return False

if __name__ == "__main__":
    main()
