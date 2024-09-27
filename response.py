from validator_collection import validators, checkers, errors


def main():
    print(valida(input("What's your email address? ")))


def valida(s):
        

        is_email_address = checkers.is_email('this-is-an-invalid-email')

        is_email_address = checkers.is_email(s)



        if is_email_address == True:
            return "Valid"
        else:
             return "Invalid"



if __name__ == "__main__":
    main()