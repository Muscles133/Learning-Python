import inflect

p = inflect.engine()


def main():
    names = []

    while True:
        try:
            name = input("Name: ").strip().title() #prompts for name
            if name:
                names.append(name)
               
        except EOFError:
            #result = p.join(names)
            print (f"Adieu, adieu, to {p.join(names)}")
            break
        
        except KeyError:
            pass

main()


"""
mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"

mylist = p.join(("apple", "banana"))
# "apple and banana"

mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"

"""

# mylist = p.join(("apple", "banana", "carrot"))
# print(mylist)
