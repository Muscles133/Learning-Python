class CardGame:
    def __init__(self):
        self.player_hand = []
        self.discard_pile = []
        self.min_set_size = 3
        self.max_set_size = 6
        
    def add_cards_to_hand(self, cards):
        """Add cards to player's hand"""
        self.player_hand.extend(cards)
    
    def find_sets(self):
        """Find all possible sets and runs"""
        return {
            'character_sets': self._find_character_sets(),
            'number_sets': self._find_number_sets(),
            'runs': self._find_runs()
        }
    
    def _find_character_sets(self):
        """Find sets of cards with matching characters (3-6 cards)"""
        character_groups = {}
        sets = []
        
        # Group cards by character
        for card in self.player_hand:
            char, num = card
            if char not in character_groups:
                character_groups[char] = []
            character_groups[char].append(card)
        
        # Find valid sets of different sizes
        for cards in character_groups.values():
            for size in range(self.min_set_size, self.max_set_size + 1):
                if len(cards) >= size:
                    sets.append({
                        'cards': cards[:size],
                        'size': size,
                        'type': 'character'
                    })
        
        return sets
    
    def _find_number_sets(self):
        """Find sets of cards with matching numbers (3-6 cards)"""
        number_groups = {}
        sets = []
        
        # Group cards by number
        for card in self.player_hand:
            char, num = card
            if num not in number_groups:
                number_groups[num] = []
            number_groups[num].append(card)
        
        # Find valid sets of different sizes
        for cards in number_groups.values():
            for size in range(self.min_set_size, self.max_set_size + 1):
                if len(cards) >= size:
                    sets.append({
                        'cards': cards[:size],
                        'size': size,
                        'type': 'number'
                    })
        
        return sets
    
    def _find_runs(self):
        """Find runs of consecutive numbers (3+ cards of same character)"""
        character_groups = {}
        runs = []
        
        # Group cards by character
        for card in self.player_hand:
            char, num = card
            if char not in character_groups:
                character_groups[char] = []
            character_groups[char].append(card)
        
        # Find runs for each character
        for char, cards in character_groups.items():
            # Sort cards by number
            sorted_cards = sorted(cards, key=lambda x: x[1])
            numbers = [card[1] for card in sorted_cards]
            
            # Find all possible runs
            for start_idx in range(len(numbers)):
                current_run = [sorted_cards[start_idx]]
                current_num = numbers[start_idx]
                
                for i in range(start_idx + 1, len(numbers)):
                    if numbers[i] == current_num + 1:
                        current_run.append(sorted_cards[i])
                        current_num = numbers[i]
                    elif numbers[i] > current_num + 1:
                        break
                
                if len(current_run) >= self.min_set_size:
                    runs.append({
                        'cards': current_run,
                        'size': len(current_run),
                        'type': 'run'
                    })
        
        return runs
    
    def remove_set(self, set_type, set_index):
        """Remove a set from player's hand and add to discard pile"""
        sets = self.find_sets()
        try:
            if set_type == 'c':
                cards_to_remove = sets['character_sets'][set_index]['cards']
            elif set_type == 'n':
                cards_to_remove = sets['number_sets'][set_index]['cards']
            elif set_type == 'r':
                cards_to_remove = sets['runs'][set_index]['cards']
            else:
                return False
            
            # Remove cards from hand and add to discard
            for card in cards_to_remove:
                self.player_hand.remove(card)
                self.discard_pile.append(card)
            return True
        except (IndexError, KeyError):
            return False
    
    def display_hand(self):
        """Display the current hand"""
        print("\nPlayer's hand:")
        sorted_hand = sorted(self.player_hand, key=lambda x: (x[0], x[1]))
        for char, num in sorted_hand:
            print(f"{char}: {num}")
    
    def display_sets(self):
        """Display all available sets and runs"""
        sets = self.find_sets()
        
        if not any(sets.values()):
            print("No sets or runs available!")
            return False
        
        if sets['character_sets']:
            print("\nCharacter sets (enter 'c0', 'c1', etc.):")
            for i, set_info in enumerate(sets['character_sets']):
                cards = set_info['cards']
                char = cards[0][0]
                numbers = [card[1] for card in cards]
                print(f"c{i}. {char}: {set_info['size']} cards with numbers {numbers}")
        
        if sets['number_sets']:
            print("\nNumber sets (enter 'n0', 'n1', etc.):")
            for i, set_info in enumerate(sets['number_sets']):
                cards = set_info['cards']
                num = cards[0][1]
                chars = [card[0] for card in cards]
                print(f"n{i}. Number {num}: {set_info['size']} cards with characters {chars}")
        
        if sets['runs']:
            print("\nRuns (enter 'r0', 'r1', etc.):")
            for i, run_info in enumerate(sets['runs']):
                cards = run_info['cards']
                char = cards[0][0]
                numbers = [card[1] for card in cards]
                print(f"r{i}. {char}: {run_info['size']} cards with numbers {numbers}")
        
        return True

# def test_game():
#     # Create test hand with potential runs and various set sizes
#     test_hand = [
#         ("Blue Sorceress", 5),
#         ("Blue Sorceress", 6),
#         ("Blue Sorceress", 7),  # Run of 3
#         ("Blue Sorceress", 8),  # Makes it a run of 4
#         ("Orange Rogue", 4),
#         ("Purple Warrior", 4),
#         ("Green Ranger", 4),
#         ("Yellow Mage", 4),     # 4 cards with number 4
#         ("Orange Rogue", 7),
#         ("Orange Rogue", 9),
#         ("Orange Rogue", 10),   # Multiple Orange Rogue cards
#     ]
    
#     # Create game instance
#     game = CardGame()
#     game.add_cards_to_hand(test_hand)
    
#     # Main game loop
#     while True:
#         game.display_hand()
#         if not game.display_sets():
#             break
            
#         choice = input("\nEnter set to remove (e.g., 'c0', 'n0', 'r0'), or press Enter to stop: ").lower()
#         if not choice:
#             break
            
#         set_type = choice[0]
#         try:
#             set_index = int(choice[1:])
#             if game.remove_set(set_type, set_index):
#                 print("\nSet removed successfully!")
#                 print("Discard pile:", game.discard_pile)
#             else:
#                 print("\nFailed to remove set. Please try again.")
#         except ValueError:
#             print("\nInvalid choice! Please use format 'c0', 'n0', or 'r0'")

# if __name__ == "__main__":
#     test_game()