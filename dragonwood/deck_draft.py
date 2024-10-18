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
    
    def select_cards(self, input_string):
        """this selects a card from the adventure deck. removed it and places it in the players hand"""
        # Remove all spaces and commas
        cleaned_input = ''.join(input_string.replace(',', '').split())
        
        # Check if all characters are digits
        if not cleaned_input.isdigit():
            raise ValueError("Input must contain only numbers, spaces, or commas")
        
        # Convert to list of integers
        numbers = [int(num) for num in cleaned_input]
        
        # Validate each number is 1-9
        if not all(1 <= num <= 9 for num in numbers):
            raise ValueError("Numbers must be between 1 and 9")
        
        # Check for unique numbers
        if len(numbers) != len(set(numbers)):
            raise ValueError("Numbers must be unique")
        
        # Check length constraints
        if not (3 <= len(numbers) <= 6):
            raise ValueError("Must provide between 3 and 6 numbers")
        
        # Convert to zero-based indices
        selection = [num - 1 for num in numbers]
        
        # Important: Use self._chosen_cards instead of self.chosen_cards
        self._chosen_cards = [self._hand[i] for i in selection]
        return self._chosen_cards

    def process_scream(self):
        """Process matching cards and update hand for scream(same characters) deletes selected matched cards from hand."""
        if not self._chosen_cards or len(self._chosen_cards) < 3:
            return False
        
        if not self._chosen_cards or len(self._chosen_cards) > 6:
            return False

        # Get the character of the first card
        target_char = self._chosen_cards[0][0]
        
        # Check if first three - six cards match
        if len(self._chosen_cards) == 3:
            first_three_match = all(card[0] == target_char for card in self._chosen_cards[:3])

            if first_three_match:
            # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:3]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 3
                self._attacktype = "Scream"
                return True
            
        elif len(self._chosen_cards) == 4:
            first_four_match = all(card[0] == target_char for card in self._chosen_cards[:4])

            if first_four_match:
                # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:4]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 4
                self._attacktype = "Scream"
                return True
            
        elif len(self._chosen_cards) == 5:
            first_five_match = all(card[0] == target_char for card in self._chosen_cards[:5])
            if first_five_match:
            # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:5]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 5
                self._attacktype = "Scream"
                return True
            
        elif len(self._chosen_cards) == 6:
            first_six_match = all(card[0] == target_char for card in self._chosen_cards[:6])

            if first_six_match:
            # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:6]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 6
                self._attacktype = "Scream"
                return True
        return False
    
    def process_stomp(self):
        """Process matching cards and update hand for stomps(match same number) deletes selected matched cards from hand."""
        if not self._chosen_cards or len(self._chosen_cards) < 3:
            return False
        
        if not self._chosen_cards or len(self._chosen_cards) > 6:
            return False

        # Get the character of the first card
        target_char = self._chosen_cards[0][1]
        
        # Check if first three - six cards match
        if len(self._chosen_cards) == 3:
            first_three_match = all(card[1] == target_char for card in self._chosen_cards[:3])

            if first_three_match:
            # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:3]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 3
                self._attacktype = "Stomp"
                return True
            
        elif len(self._chosen_cards) == 4:
            first_four_match = all(card[0] == target_char for card in self._chosen_cards[:4])

            if first_four_match:
                # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:4]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 4
                self._attacktype = "Stomp"
                
                return True
            
        elif len(self._chosen_cards) == 5:
            first_five_match = all(card[0] == target_char for card in self._chosen_cards[:5])
            if first_five_match:
            # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:5]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 5
                self._attacktype = "Stomp"
                return True
            
        elif len(self._chosen_cards) == 6:
            first_six_match = all(card[0] == target_char for card in self._chosen_cards[:6])

            if first_six_match:
            # Remove matched cards from hand
                cards_to_remove = self._chosen_cards[:6]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 6
                self._attacktype = "Stomp"
                return True
        return False
    


    def process_strike(self):
        """Process matching cards and update hand for strikes (runs) deletes selected matched cards from hand."""
        if not self._chosen_cards or len(self._chosen_cards) < 3:
            return False
        
        if not self._chosen_cards or len(self._chosen_cards) > 6:
            return False
        
        #sort list

        sorted_data = sorted(self._chosen_cards, key=lambda x: x[1])
        run_length=3

        for i in range(len(sorted_data) - run_length + 1):
            if all(sorted_data[i+j][1] == sorted_data[i][1] + j for j in range(run_length)):
                #return True # this makes it true to grab cards and delete
                cards_to_remove = self._chosen_cards[:3]
                for card in cards_to_remove:
                    if card in self._hand:
                        self._hand.remove(card)
                self._num_dice = 3
                self._attacktype = "Strike"
                return True
            
        return False






def main():
    dk = Deck()
    
    # Draw 9 cards
    for _ in range(9):
        dk.pick()

    
    dk.hand()
    
    while True:
        try:
            choose = input("\nMake a selection (e.g., '1,2,3' or '123'): ")
            dk.select_cards(choose)
            if dk.process_scream():
                print(f"You {dk.attacktype()} at the monster with {dk.dice_rolled()} dice rolled!")
                dk.dice_rolled()
                print("\nUpdated hand:")
                dk.hand()

            elif dk.process_stomp():
                print("\nMatch found!")
                dk.dice_rolled()
                print("\nUpdated hand:")
                dk.hand()

            elif dk.process_strike():
                print(f"You {dk.attacktype()} at the monster with {dk.dice_rolled()} dice rolled!")
                dk.dice_rolled()
                print("\nUpdated hand:")
                dk.hand()



            else:
                print("\nNo match found.")
                dk.hand()
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()