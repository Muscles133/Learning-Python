
import random

class Deck:
    def __init__(self):
        # build deck
        self._deck = []
        self._hand = []
        self._chosen_cards = []
        self._num_dice = 0
        self._attacktype = ""
        
        characters = ["Blue Sorceress", "Orange Rogue", "Purple Warrior", "Green Ranger"]
        for character in characters:
            for value in range(1, 13):  # 1 to 12
                self._deck.append((character, value))

    @property
    def deck(self):
        return self._deck
    
    def dice_rolled(self):
        return self._num_dice

    def attacktype(self):
        return self._attacktype
    
    def hand(self):
        print("Your hand:")
        for i, card in enumerate(self._hand):
            print(f"{i+1}. {card[0]} of {card[1]}")

    def pick(self):
        if len(self._deck) > 0 and len(self._hand) < 9:
            random_index = random.randint(0, len(self._deck) - 1)
            item = self._deck.pop(random_index)
            self._hand.append(item)
            return True
        return False
    


# def process_strike(self):
#     """Process matching cards and update hand for strikes (runs) deletes selected matched cards from hand."""
#     if not self._chosen_cards or len(self._chosen_cards) < 3:
#         return False
    
#     if not self._chosen_cards or len(self._chosen_cards) > 6:
#         return False
    
#     #sort list

#     sort_select = for numb in sorted(self._chosen_cards, key

#     # for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
# #     print(gryffindor["name"])



#     # Get the number of the first card
#     target_number = int(self._chosen_cards[0][1])
    
#     # Check if first three - six cards match
#     if len(self._chosen_cards) == 3:
#         first_three_match = all(card[1] == target_char for card in self._chosen_cards[:3])

#         if first_three_match:
#         # Remove matched cards from hand
#             cards_to_remove = self._chosen_cards[:3]
#             for card in cards_to_remove:
#                 if card in self._hand:
#                     self._hand.remove(card)
#             self._num_dice = 3
#             self._attacktype = "Stomp"
#             return True
        
#     return False



def main():

    dk = Deck()

    handz = [("Orange Rogue", 1),("Orange Rogue", 2),("Orange Rogue", 3)]
    print (handz)






if __name__ == "__main__":
    main()