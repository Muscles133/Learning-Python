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

        self.start_deck = []
        # Create all monster instances
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
        
        # Build the deck with the correct number of copies

        self._build_deck()
        self.deck = []
        
        
        self.discard_deck = []
        self.collected_deck = []
        self.landscape = []
        
    def _build_deck(self):
        # Dictionary defining how many copies of each monster should be in the deck
        quantities = {
            'ss': 4, 'od': 1, 'bd': 1, 'hb': 2, 'fj': 2, 'cb': 4,
            'wn': 2, 'pw': 2, 'secs': 1, 'fa': 2, 'wb': 2, 'gg': 2,
            'gt': 1, 'goog': 1, 'ag': 1, 'gp': 1
        }
        
        # Add the correct number of copies of each monster to the deck
        for monster_key, quantity in quantities.items():
            for _ in range(quantity):
                self.start_deck.append(self.monsters[monster_key])

        # Grab random cards and delete them

        # random_index = random.randint(0, len(self.start_deck) -1)
        # item = self.start_deck.pop(random_index)
        # self.deck.append(item)

        Monster_deck.shuffle(self)

        for _ in range(5):
            Monster_deck.del_draw(self)


    @property
    def deck(self):
        return self.start_deck
    @property
    def discard_deck(self):
        return self.discard_deck





    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.deck)
    
    def draw(self):
        """Draw a card from the deck put on landscape"""
        if len(self.deck) > 0:
            item = self.deck.pop()
            self.landscape.append(item)
        return None
    
    def del_draw(self):
        """Draw a card from the deck put in bin"""
        if len(self.deck) > 0:
            item = self.deck.pop()
            self.discard_deck.append(item)
        return None


    
    def alive_landscape(self):
        if len(self.landscape) > 0:
            print(self.landscape)


    
    def get_deck_size(self):
        """Return the current size of the deck"""
        return len(self.deck)

def main():
    # Create a new monster deck
    monster_deck = Monster_deck()
    
    # You can now use the deck like this:
    monster_deck.shuffle()
    
    # Example of drawing a card
    drawn_monster = monster_deck.draw()
    if drawn_monster:
        print(f"Drew a {drawn_monster.name}")
    
    # Check remaining cards
    print(f"Remaining cards: {monster_deck.alive_landscape()}")

if __name__ == "__main__":
    main()