import random

class Monster:
    def __init__(self, name, score, strike, stomp, scream):
        self.name = name
        self.score = score
        self.strike = strike
        self.stomp = stomp
        self.scream = scream

    def __str__(self):
        return self.name

class Monster_deck:
    def __init__(self):
        # Initialize all deck lists
        self.main_deck = []
        self.deleted_cards = []  # For the 10 removed cards
        self.landscape = []      # For cards in play
        self.discard_pile = []   # For discarded cards
        
        # Create all monster instances and build initial deck
        self.monsters = {
            'ss': Monster("Spooky Spiders", 1, 3, 3, 4),
            'od': Monster("Orange Dragon", 7, 15, 11, 12),
            'bd': Monster("Blue Dragon", 6, 13, 10, 13),
            'hb': Monster("Hungry Bear", 3, 7, 6, 9),
            'fj': Monster("Fierce Jaguar", 3, 8, 6, 8),
            'cb': Monster("Crazy Bats", 1, 4, 3, 3),
            'wn': Monster("Wasps' Nest", 2, 5, 6, 7),
            'pw': Monster("Pack of Wolves", 3, 6, 7, 9),
            'secs': Monster("Secret Shadow", 4, 10, 8, 11),
            'fa': Monster("Fire Ants", 2, 7, 4, 6),
            'wb': Monster("Wild Boar", 3, 8, 7, 7),
            'gg': Monster("Giggling Goblin", 2, 7, 5, 5),
            'gt': Monster("Grumpy Troll", 4, 9, 11, 9),
            'goog': Monster("Gooey Glob", 5, 14, 9, 10),
            'ag': Monster("Angry Ogre", 5, 12, 9, 14),
            'gp': Monster("Gigantic Python", 4, 11, 8, 10)
        }
        
        self._build_deck()
        self._initialize_game()
        
    def _build_deck(self):
        """Builds the initial full deck"""
        quantities = {
            'ss': 4, 'od': 1, 'bd': 1, 'hb': 2, 'fj': 2, 'cb': 4,
            'wn': 2, 'pw': 2, 'secs': 1, 'fa': 2, 'wb': 2, 'gg': 2,
            'gt': 1, 'goog': 1, 'ag': 1, 'gp': 1
        }
        
        for monster_key, quantity in quantities.items():
            for _ in range(quantity):
                self.main_deck.append(self.monsters[monster_key])

    def _initialize_game(self):
        """Shuffles deck and removes 10 cards to deleted_cards"""
        random.shuffle(self.main_deck)
        for _ in range(10):
            if self.main_deck:  # Check if deck is not empty
                self.deleted_cards.append(self.main_deck.pop())

    def draw_to_landscape(self):
        """Draws a card from main deck to landscape"""
        if self.main_deck:
            drawn_card = self.main_deck.pop()
            self.landscape.append(drawn_card)
            return drawn_card
        return None

    def discard_from_landscape(self, monster_name):
        """Moves a specific monster from landscape to capture deck"""
        for monster in self.landscape:
            if monster.name == monster_name:
                self.landscape.remove(monster)
                self.discard_pile.append(monster)
                return True
        return False
    
    def disp_landscape(self):
        for i, no in enumerate(range(5)):
            letter = chr(ord('A') + i)
            print(f"Landscape: [{letter}] {self.landscape[no].name} **Capture value {self.landscape[no].score} **Strike of {self.landscape[no].strike} **Stomp of {self.landscape[no].stomp} **Scream of {self.landscape[no].scream}")

    def select_mon(self, a):

        if a == "a":
            return self.landscape[0]

        elif a == "b":
            return self.landscape[1]

        elif a == "c":
            return self.landscape[2]

        elif a == "d":
            return self.landscape[3]

        elif a == "e":
            return self.landscape[4]

        return False
    






    def get_deck_sizes(self):
        """Returns the current size of all decks"""
        return {
            'main_deck': len(self.main_deck),
            'deleted_cards': len(self.deleted_cards),
            'landscape': len(self.landscape),
            'discard_pile': len(self.discard_pile)
        }

    def display_landscape(self):
        """Displays all monsters currently in the landscape"""
        return [monster.name for monster in self.landscape]

def main():
    # Create a new monster deck (automatically shuffles and removes 10 cards)
    monster_deck = Monster_deck()
    
    # Print initial deck sizes
    print("Initial deck sizes:", monster_deck.get_deck_sizes())
    
    # Draw some cards to landscape
    for _ in range(3):
        drawn = monster_deck.draw_to_landscape()
        if drawn:
            print(f"Landscape: {drawn.name} **Capture value {drawn.score} **Strike of {drawn.strike} **Stomp of {drawn.stomp} **Scream of {drawn.scream}")
    
    # Display current landscape
    print("\nCurrent landscape:", monster_deck.display_landscape())
    
    # Discard a monster from landscape (if it exists)
    if monster_deck.landscape:
        monster_to_discard = monster_deck.landscape[0].name
        if monster_deck.discard_from_landscape(monster_to_discard):
            print(f"\nDiscarded {monster_to_discard} from landscape")
    
    # Print final deck sizes
    print("\nFinal deck sizes:", monster_deck.get_deck_sizes())



    

if __name__ == "__main__":
    main()
    pass