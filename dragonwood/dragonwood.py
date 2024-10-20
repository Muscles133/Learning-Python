# game.py
import random
from monster_deck import Monster, Monster_deck
from adventure_deck import Deck

#global things
md= Monster_deck()  # md is short for monster deck
ad = Deck() #ad is short for adventure deck


def main():

     # Draw some cards to landscape
    for _ in range(5):
        md.draw_to_landscape()
    md.disp_landscape()
        #if drawn:
        #    print(f"Landscape: {drawn.name} **Capture value {drawn.score} **Strike of {drawn.strike} **Stomp of {drawn.stomp} **Scream of {drawn.scream}")

    print("") #gives a space

    #print(monster_deck.display_landscape())

    # Draw 5 cards
    for _ in range(5):
        ad.pick()
    ad.hand()

    print("")

    print("\nThe battle for dragonwood has begun!")

    # while md.get_ls_size() != 0:
    #     choose()

    while ad.repack() != 2 or md.get_ls_size() != 0:
        choose()

    print('')

    print(f"Dragonwood has been defeated your final score is: {md.ret_score()}")




def roll():
    """This is the chances for a 6 sided dice with only 4 values. The upper and lower values have less chance"""
    num = [1, 2, 3, 4]
    fra = 100 / 6
    roll = random.choices(num, weights=[fra, fra * 2, fra * 2, fra])[0]
    return roll

def roll_outcome(x):
    """This rolls the four sided dice to the ammount of cards used in the attack"""
    tot = 0
    for _ in range(x):
        tot += roll()
    return tot

# def compare_attack(roll_val, mon_val):
#     if not roll_val > mon_val:  #if the roll fails


def what_mon():
    selection = str(input("What do you want to attack? "))
    mon_selected = md.select_mon(selection)
    return mon_selected

def compare_attack(x, y):  #true if x is greater or equeal to y
    if x >= y:
        return True
    else:
        return False
    
def validate_input(input_string):
    input_string = input_string.lower()
    input_set = set(input_string)
    valid_letters = set('abcdefghi')
    
    # Check three conditions:
    is_valid_chars = input_set.issubset(valid_letters)  # Only contains a-i
    is_long_enough = len(input_string) >= 3             # 3 or more chars
    no_duplicates = len(input_string) == len(input_set) # All unique
    
    if is_valid_chars and is_long_enough and no_duplicates:
        return True
    return False





def choose():
    while True:
        try:
            choose = input("\nAttack monster with a Strike, Stomp, Scream or 'p' for pick a card: ").lower()
            print("")
            if validate_input(choose) == True:
                mon = what_mon()



                ad.select_cards(choose)

                if ad.process_scream():
                    print(f"You {ad.attacktype()} at the monster with {ad.dice_rolled()} dice rolled!")
                    result = roll_outcome(ad.dice_rolled())
                    #print(f"Your total value is: {result} Attack points")
                    attack_num = md.mon_scream(mon)
                    if compare_attack(result, attack_num) == True:
                        md.discard_from_landscape(mon.name)
                        md.draw_to_landscape()
                        print(f"Success you captured {mon.name} with an attack roll of {result} you only needed {attack_num}")
                        
                        print(f"Current Score: {md.ret_score()}")
                        print("")
                        md.disp_landscape()

                    else:
                        print(f"Failed to capture: {mon.name} required {attack_num} you only achieved {result}")


                elif ad.process_stomp():
                    print(f"You {ad.attacktype()} at the monster with {ad.dice_rolled()} dice rolled!")
                    result = roll_outcome(ad.dice_rolled())
                    #print(f"Your total value is: {result} Attack points")
                    attack_num = md.mon_stomp(mon)
                    if compare_attack(result, attack_num) == True:
                        md.discard_from_landscape(mon.name)
                        md.draw_to_landscape()
                        print(f"Success you captured {mon.name} with an attack roll of {result} you only needed {attack_num}")
                        
                        print(f"Current Score: {md.ret_score()}")
                        print("")
                        md.disp_landscape()

                    else:
                        print(f"Failed to capture: {mon.name} required {attack_num} you only achieved {result}")
                    

                elif ad.process_strike():
                    print(f"You {ad.attacktype()} at the monster with {ad.dice_rolled()} dice rolled!")
                    #print(f"Your total value is: {result} Attack points")
                    attack_num = md.mon_strike(mon)
                    if compare_attack(result, attack_num) == True:
                        md.discard_from_landscape(mon.name)
                        md.draw_to_landscape()
                        print(f"Success you captured {mon.name} with an attack roll of {result} you only needed {attack_num}")
                        
                        print(f"Current Score: {md.ret_score()}")
                        print("")
                        md.disp_landscape()

                    else:
                        print(f"Failed to capture: {mon.name} required {attack_num} you only achieved {result}")

                else:
                    print("\nNo match found. or wrong imput. Have a card instead")
                    ad.pick()
                    ad.hand()

            elif choose.lower() == "p":
                ad.pick()
                print("You gain a card")
                ad.hand()
                

            else:
                ad.pick()
                print("Valid inputs are 'p' or 123, 5555, 6793 etc.... im going to give u are card.")
                ad.hand()


            

            break
        except ValueError as e:
            print(f"Error: {e}")
            continue

    
    
if __name__ == "__main__":
    main()