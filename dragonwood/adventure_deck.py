import random
from rich import print
from rich.console import Console
from rich.table import Table
from rich import box


class Deck:
    def __init__(self):
        # build deck
        self._deck = []
        self._hand = []
        self._chosen_cards = []
        self._num_dice = 0
        self._attacktype = ""
        self._repack = 0
        Deck.rebuild_deck(self)

        # characters = ["Blue Sorceress", "Orange Rogue", "Purple Warrior", "Green Ranger"]
        # for character in characters:
        #     for value in range(1, 13):  # 1 to 12
        #         self._deck.append((character, value))

    @property
    def deck(self):
        return self._deck

    def dice_rolled(self):
        return self._num_dice

    def attacktype(self):
        return self._attacktype

    def repack(self):
        return self._repack

    def rebuild_deck(self):
        characters = [
            "Blue Sorceress",
            "Orange Rogue",
            "Purple Warrior",
            "Green Ranger",
        ]
        for character in characters:
            for value in range(1, 13):  # 1 to 12
                self._deck.append((character, value))

    def hand(self):
        console = Console()

        # Create a table for the hand
        hand_table = Table(
            title="[bold magenta]Adventure Cards",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold cyan",
        )

        # Add columns
        hand_table.add_column("Card", style="cyan")
        hand_table.add_column("Character", style="bright_green")
        hand_table.add_column("Value", style="yellow")

        # Add each card to the table
        for i, card in enumerate(self._hand):
            letter = chr(ord("A") + i)
            # Add color styling based on character type
            character_color = self._get_character_color(card[0])
            hand_table.add_row(
                f"[{letter}]",
                f"[{character_color}]{card[0]}[/{character_color}]",
                str(card[1]),
            )

        # Print the table
        console.print(hand_table)

    def _get_character_color(self, character):
        # Helper method to return the appropriate color for each character type
        color_map = {
            "Blue Sorceress": "turquoise2",
            "Orange Rogue": "orange1",
            "Purple Warrior": "purple",
            "Green Ranger": "sea_green2",
        }
        return color_map.get(character, "white")

    def pick(self):
        if len(self._deck) > 0 and len(self._hand) < 9:
            random_index = random.randint(0, len(self._deck) - 1)
            item = self._deck.pop(random_index)
            self._hand.append(item)
            return True
        elif len(self._deck) == 0 and len(self._hand) < 9:
            Deck.rebuild_deck(self)
            self._repack += 1
            random_index = random.randint(0, len(self._deck) - 1)
            item = self._deck.pop(random_index)
            self._hand.append(item)
            return True

        elif len(self._hand) >= 9:
            print("You cant have more than 9 cards")

            random.shuffle(self._hand)
            for _ in range(1):
                if self._hand:  # Check if deck is not empty
                    self._hand.pop()
            return True

        return False

    def select_cards(self, input_string):
        """This selects a card from the adventure deck, removes it and places it in the player's hand"""
        # Remove all spaces and commas
        cleaned_input = "".join(input_string.replace(",", "").split()).lower()

        # Replace letters with numbers
        converted = (
            cleaned_input.replace("a", "1")
            .replace("b", "2")
            .replace("c", "3")
            .replace("d", "4")
            .replace("e", "5")
            .replace("f", "6")
            .replace("g", "7")
            .replace("h", "8")
            .replace("i", "9")
        )
        # print(f"Converted string: {converted}")

        # Convert to list of integers
        numbers = [int(num) for num in converted]
        # print(f"Numbers list: {numbers}")

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
            first_three_match = all(
                card[0] == target_char for card in self._chosen_cards[:3]
            )

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
            first_four_match = all(
                card[0] == target_char for card in self._chosen_cards[:4]
            )

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
            first_five_match = all(
                card[0] == target_char for card in self._chosen_cards[:5]
            )
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
            first_six_match = all(
                card[0] == target_char for card in self._chosen_cards[:6]
            )

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
            first_three_match = all(
                card[1] == target_char for card in self._chosen_cards[:3]
            )

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
            first_four_match = all(
                card[0] == target_char for card in self._chosen_cards[:4]
            )

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
            first_five_match = all(
                card[0] == target_char for card in self._chosen_cards[:5]
            )
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
            first_six_match = all(
                card[0] == target_char for card in self._chosen_cards[:6]
            )

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

        if len(self._chosen_cards) == 3:
            sorted_data = sorted(self._chosen_cards, key=lambda x: x[1])  # sort list
            run_length = 3

            for i in range(len(sorted_data) - run_length + 1):
                if all(
                    sorted_data[i + j][1] == sorted_data[i][1] + j
                    for j in range(run_length)
                ):
                    # return True # this makes it true to grab cards and delete
                    cards_to_remove = self._chosen_cards[:3]
                    for card in cards_to_remove:
                        if card in self._hand:
                            self._hand.remove(card)
                    self._num_dice = 3
                    self._attacktype = "Strike"
                    return True
            return False

        elif len(self._chosen_cards) == 4:
            sorted_data = sorted(self._chosen_cards, key=lambda x: x[1])  # sort list
            run_length = 4

            for i in range(len(sorted_data) - run_length + 1):
                if all(
                    sorted_data[i + j][1] == sorted_data[i][1] + j
                    for j in range(run_length)
                ):
                    # return True # this makes it true to grab cards and delete
                    cards_to_remove = self._chosen_cards[:4]
                    for card in cards_to_remove:
                        if card in self._hand:
                            self._hand.remove(card)
                    self._num_dice = 4
                    self._attacktype = "Strike"
                    return True
            return False

        elif len(self._chosen_cards) == 5:
            sorted_data = sorted(self._chosen_cards, key=lambda x: x[1])  # sort list
            run_length = 5

            for i in range(len(sorted_data) - run_length + 1):
                if all(
                    sorted_data[i + j][1] == sorted_data[i][1] + j
                    for j in range(run_length)
                ):
                    # return True # this makes it true to grab cards and delete
                    cards_to_remove = self._chosen_cards[:5]
                    for card in cards_to_remove:
                        if card in self._hand:
                            self._hand.remove(card)
                    self._num_dice = 5
                    self._attacktype = "Strike"
                    return True
            return False

        elif len(self._chosen_cards) == 6:
            sorted_data = sorted(self._chosen_cards, key=lambda x: x[1])  # sort list
            run_length = 6

            for i in range(len(sorted_data) - run_length + 1):
                if all(
                    sorted_data[i + j][1] == sorted_data[i][1] + j
                    for j in range(run_length)
                ):
                    # return True # this makes it true to grab cards and delete
                    cards_to_remove = self._chosen_cards[:6]
                    for card in cards_to_remove:
                        if card in self._hand:
                            self._hand.remove(card)
                    self._num_dice = 6
                    self._attacktype = "Strike"
                    return True
            return False


def main():
    ad = Deck()

    # Draw 9 cards
    for _ in range(9):
        ad.pick()

    ad.hand()

    print("")

    print(ad.repack())


if __name__ == "__main__":
    main()
    pass
