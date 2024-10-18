import random

class Monster:
    def __init__(self, name, score, strike, stomp, scream):
        self.name = name
        self.score = score
        self.strike = strike
        self.stomp = stomp
        self.scream = scream

    def __str__(self):
        return f"{self.name} has {self.score} points. Attck with STRIKE of {self.strike}, STOMP of {self.stomp}, SCREAM of {self.scream}"

class CardGame:
    def __init__(self):
        self.player_hand = []
        self.discard_pile = []
        self.min_set_size = 3
        self.max_set_size = 6
        self.landscape = []
        self.mon_dis = []
        self.roll = 0

    def display_hand(self):
        """Display the player's current hand."""
        print("Your hand:")
        for i, card in enumerate(self.player_hand):
            print(f"{i}. {card[0]}: {card[1]}")

    def find_sets(self):
        """Find and return all sets and runs available in the player's hand."""
        # Placeholder for find_sets logic
        character_sets = self._find_character_sets()
        number_sets = self._find_number_sets()
        runs = self._find_runs()
        
        return {
            'character_sets': character_sets,
            'number_sets': number_sets,
            'runs': runs
        }

    def _find_character_sets(self):
        """Find sets of cards with the same character."""
        sets = []
        character_groups = {}
        
        # Group cards by character
        for card in self.player_hand:
            char, num = card
            if char not in character_groups:
                character_groups[char] = []
            character_groups[char].append(card)
        
        # Add valid sets to the list
        for char, cards in character_groups.items():
            if len(cards) >= self.min_set_size:
                sets.append({
                    'cards': cards,
                    'size': len(cards),
                    'type': 'character_set'
                })
        
        return sets

    def _find_number_sets(self):
        """Find sets of cards with the same number."""
        sets = []
        number_groups = {}
        
        # Group cards by number
        for card in self.player_hand:
            char, num = card
            if num not in number_groups:
                number_groups[num] = []
            number_groups[num].append(card)
        
        # Add valid sets to the list
        for num, cards in number_groups.items():
            if len(cards) >= self.min_set_size:
                sets.append({
                    'cards': cards,
                    'size': len(cards),
                    'type': 'number_set'
                })
        
        return sets

    def _find_runs(self):
        """Find runs of consecutive numbers regardless of character."""
        runs = []
        
        # Sort all cards by number
        sorted_cards = sorted(self.player_hand, key=lambda x: x[1])
        
        # Group cards by number
        number_groups = {}
        for card in sorted_cards:
            char, num = card
            if num not in number_groups:
                number_groups[num] = []
            number_groups[num].append(card)
        
        # Find all possible number sequences
        numbers = sorted(list(number_groups.keys()))
        
        # Check each possible starting number
        for start_idx in range(len(numbers)):
            start_num = numbers[start_idx]
            current_run = []
            
            # Add all cards of the starting number
            current_run.extend(number_groups[start_num])
            
            # Look for consecutive numbers
            current_num = start_num
            for next_num in numbers[start_idx + 1:]:
                if next_num == current_num + 1:
                    current_run.extend(number_groups[next_num])
                    current_num = next_num
                else:
                    break
            
            # If we have enough cards for a run
            if len(set(card[1] for card in current_run)) >= self.min_set_size:
                # Take one card from each number to form runs
                basic_run = []
                run_numbers = sorted(set(card[1] for card in current_run))
                for num in run_numbers:
                    basic_run.append(number_groups[num][0])  # Take first card of each number
                
                runs.append({
                    'cards': basic_run,
                    'size': len(basic_run),
                    'type': 'run'
                })
        
        return runs

    def remove_set(self, set_type, set_index):
        """Remove a set or run from the player's hand."""
        sets = self.find_sets()
        if set_type == 'c':
            selected_set = sets['character_sets'][set_index]
        elif set_type == 'n':
            selected_set = sets['number_sets'][set_index]
        elif set_type == 'r':
            selected_set = sets['runs'][set_index]
        else:
            return False
        
        # Return a number to roll dice
        for count in range(len(selected_set)):
            count += 1
            self.roll = count
        
        # Remove cards from the player's hand and add to discard pile
        for card in selected_set['cards']:
            self.player_hand.remove(card)
            self.discard_pile.append(card)
        
        return True
    
    @property
    def roll(self):
        return self._roll
    
    @roll.setter
    def roll(self, value):
        self._roll = value

    def display_sets(self):
        """Display all available sets and runs."""
        sets = self.find_sets()
        
        if not any(sets.values()):
            print("No sets or runs available!")
            return False
        
        if sets['character_sets']: #Scream!
            print("\nCharacter sets (enter 'c0', 'c1', etc.):")
            for i, set_info in enumerate(sets['character_sets']):
                cards = set_info['cards']
                char = cards[0][0]
                numbers = [card[1] for card in cards]
                print(f"c{i}. Scream with {numbers}")
        
        if sets['number_sets']: #stomp!
            print("\nNumber sets (enter 'n0', 'n1', etc.):")
            for i, set_info in enumerate(sets['number_sets']):
                cards = set_info['cards']
                num = cards[0][1]
                chars = [card[0] for card in cards]
                print(f"n{i}. Number {num}: {set_info['size']} cards with characters {chars}")
        
        if sets['runs']: #strike!
            print("\nRuns (enter 'r0', 'r1', etc.):")
            for i, run_info in enumerate(sets['runs']):
                cards = run_info['cards']
                numbers = [card[1] for card in cards]
                chars = [card[0] for card in cards]
                print(f"r{i}. Run of {run_info['size']}: {numbers}")
                print(f"    Using characters: {chars}")
        
        return True



def roll(x):
    num = [1, 2, 3, 4]
    fra = 100 / 6
    result = 0
    roll = random.choices(num, weights=[fra, fra * 2, fra * 2, fra])[0]
    for _ in range(x):
        result += roll
    return result


def get_mon(scource_list, target_list):
    if len(scource_list) > 0:
        random_index = random.randint(0, len(scource_list) - 1)
        item = scource_list.pop(random_index)
        target_list.append(item)
        return True
    return False


def move_mon(source_list, target_list, a):
    if a == "a":
        item = source_list.pop(0)
        target_list.append(item)
        return True
    elif a == "b":
        item = source_list.pop(1)
        target_list.append(item)
        return True
    elif a == "c":
        item = source_list.pop(2)
        target_list.append(item)
        return True
    elif a == "d":
        item = source_list.pop(3)
        target_list.append(item)
        return True
    elif a == "e":
        item = source_list.pop(4)
        target_list.append(item)
        return True
    return False


def select_mon(source_list, a):
    if a == "a":
        return source_list[0]

    elif a == "b":
        return source_list[1]

    elif a == "c":
        return source_list[2]

    elif a == "d":
        return source_list[3]

    elif a == "e":
        return source_list[4]

    return False

def deal_card(source_list, target_list):
        if len(source_list) > 0:
            random_index = random.randint(0, len(source_list) - 1)
            card = source_list.pop(random_index)
            target_list.append(card)
            return True
        return False

def prnt_lanscape(landscape):
    print(f"A = {landscape[0]}")
    print(f"B = {landscape[1]}")
    print(f"C = {landscape[2]}")
    print(f"D = {landscape[3]}")
    print(f"E = {landscape[4]}")
    return




def main():


    #build the adventure deck
    adventure_deck = []
    characters = ["Blue Sorceress", "Orange Rogue", "Purple Warrior", "Green Ranger"]
    for character in characters:
        for value in range(1, 13):  # 1 to 12
            adventure_deck.append((character, value))

    #build the monster deck
    ss = Monster("Spooky Spiders", 1, 3, 3, 4)  # need 4
    od = Monster("Orange Dragon", 7, 15, 11, 12)  # need 1
    bd = Monster("Blue Dragon", 6, 13, 10, 13)  # need 1
    hb = Monster("Hungry Bear", 3, 7, 6, 9)  # need 2
    fj = Monster("Fierce Jaguar", 3, 8, 6, 8)  # need 2
    cb = Monster("Crazy Bats", 1, 4, 3, 3)  # need 4
    wn = Monster("Wasps' Nest", 2, 5, 6, 7)  # need 2
    pw = Monster("Pack of Wolves", 3, 6, 7, 9)  # need 2
    secs = Monster("Secret Shadow", 4, 10, 8, 11)  # need 1
    fa = Monster("Fire Ants", 2, 7, 4, 6)  # need 2
    wb = Monster("Wild Boar", 3, 8, 7, 7)  # need 2
    gg = Monster("Giggling Goblin", 2, 7, 5, 5)  # need 2
    gt = Monster("Grumpy Troll", 4, 9, 11, 9)  # need 1
    goog = Monster("Gooey Glob", 5, 14, 9, 10)  # need 1
    ag = Monster("Angry Ogre", 5, 12, 9, 14)  # need 1
    gp = Monster("Gigantic Python", 4, 11, 8, 10)  # need 1

    mon_deck = [
        ss,
        ss,
        ss,
        ss,
        od,
        bd,
        hb,
        hb,
        fj,
        fj,
        cb,
        cb,
        cb,
        cb,
        wn,
        wn,
        pw,
        pw,
        secs,
        fa,
        fa,
        wb,
        wb,
        gg,
        gg,
        gt,
        goog,
        ag,
        gp,
    ]



    landscape = [] #monsters to attack

    mon_dis = [] #removal of monsters from the game

    #player_hand = [] #ability to strike stomp or scream

    advent_dis = [] #adventure card discard pile

    #delete 10 random monsters before the game starts
    for _ in range(10):
        get_mon(mon_deck, mon_dis)

    #populate the landscape with 5 monsters

    for _ in range(5):
        get_mon(mon_deck, landscape)

    #deal out 5 adventure cards to the players hand.

    #for _ in range(5):
    #    deal_card(adventure_deck, player_hand)

    player_hand = [
        ("Blue Sorceress", 5),
        ("Blue Sorceress", 1),
        ("Blue Sorceress", 7),  
        ("Blue Sorceress", 11),
        ("Blue Sorceress", 8), 
        ("Blue Sorceress", 8), 
    ]  





    # Create game instance
    game = CardGame()
    game.player_hand = player_hand
    
    # Main game loop
    while True:
        prnt_lanscape(landscape)
        print("")
        game.display_hand()
        if not game.display_sets():
            break
            
        choice = input("\nEnter set to remove (e.g., 'c0', 'n0', 'r0'), or press Enter to stop: ").lower()
        if not choice:
            break
            
        set_type = choice[0]
        try:
            set_index = int(choice[1:])
            if game.remove_set(set_type, set_index):
                print("\nAtacking!") #set removed succesfully
                print(f"test to remove you use {game.roll} dice")
                rolls = roll(game.roll)
                print(f"your roll is {rolls}")
                print("")
                game.display_hand()
                #print("Discard pile:", game.discard_pile)
            else:
                print("\nFailed to remove set. Please try again.")
        except ValueError:
            print("\nInvalid choice! Please use format 'c0', 'n0', or 'r0'")

if __name__ == "__main__":
    main()
