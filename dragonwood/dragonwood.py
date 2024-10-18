

import random
from cardgame import CardGame

class Monster:
    def __init__(self, name, score, strike, stomp, scream):
        self.name = name
        self.score = score
        self.strike = strike
        self.stomp = stomp
        self.scream = scream

    def __str__(self):
        return self.name
    
class Deck:
    def __init__(self):

        #build deck
        adventure_deck = []
        characters = ["Blue Sorceress", "Orange Rogue", "Purple Warrior", "Green Ranger"]
        for character in characters:
            for value in range(1, 13):  # 1 to 12
                adventure_deck.append((character, value))

        self._deck = adventure_deck

    @property
    def deck(self):
        return self._deck


def main():

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

    adventure_deck = []

    # #build the adventure deck
    # characters = ["Blue Sorceress", "Orange Rogue", "Purple Warrior", "Green Ranger"]
    # for character in characters:
    #     for value in range(1, 13):  # 1 to 12
    #         adventure_deck.append((character, value))

    landscape = [] #monsters to attack

    mon_dis = [] #removal of monsters from the game

    player_hand = [] #ability to strike stomp or scream

    advent_dis = [] #adventure card discard pile

    #delete 10 random monsters before the game starts
    for _ in range(10):
        get_mon(mon_deck, mon_dis)

    #populate the landscape with 5 monsters

    for _ in range(5):
        get_mon(mon_deck, landscape)

    #deal out 5 adventure cards to the players hand.

    for _ in range(15):
        deal_card(adventure_deck, player_hand)

        #look for sets

    # game = CardGame()
    # game.add_cards_to_hand(player_hand)
    # game.find_sets()

    # print("Player's hand:")
    # for character, value in player_hand:
    #     print(f"{character}: {value}")

    prnt_lanscape(landscape)

    attack_target = str(input("Which monster to attack? ").lower()) #make this into a try and accept loop. it must be a-e only.
    select = select_mon(landscape, attack_target)
    print(f"You are attacking the {select}")

    move_mon(landscape, mon_dis, attack_target)  # denotes you are attacking a monster
    get_mon(mon_deck, landscape)

    prnt_lanscape(landscape)

    # for mon in landscape:
    #     print(f"{mon})

    # print(landscape)


def roll():
    num = [1, 2, 3, 4]
    fra = 100 / 6
    roll = random.choices(num, weights=[fra, fra * 2, fra * 2, fra])[0]
    return roll


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

def scan_hand(player_hand):
    ...



def prnt_lanscape(landscape):
    print(f"A = {landscape[0]}")
    print(f"B = {landscape[1]}")
    print(f"C = {landscape[2]}")
    print(f"D = {landscape[3]}")
    print(f"E = {landscape[4]}")
    return


if __name__ == "__main__":
    main()