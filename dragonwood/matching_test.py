def find_matches(player_hand):
    # Initialize dictionaries to count occurrences
    character_counts = {}
    number_counts = {}
    
    # Count occurrences of characters and numbers
    for character, number in player_hand:
        # Count characters
        if character in character_counts:
            character_counts[character].append(number)
        else:
            character_counts[character] = [number]
            
        # Count numbers
        if number in number_counts:
            number_counts[number].append(character)
        else:
            number_counts[number] = [character]
    
    # Find matches (3 or more)
    matches = {
        'character_matches': [],
        'number_matches': []
    }
    
    # Check for character matches (same character, different numbers)
    for character, numbers in character_counts.items():
        if len(numbers) >= 3:
            matches['character_matches'].append({
                'character': character,
                'count': len(numbers),
                'numbers': sorted(numbers)
            })
    
    # Check for number matches (same number, different characters)
    for number, characters in number_counts.items():
        if len(characters) >= 3:
            matches['number_matches'].append({
                'number': number,
                'count': len(characters),
                'characters': sorted(characters)
            })
    
    return matches

def print_matches(matches):
    if not matches['character_matches'] and not matches['number_matches']:
        print("No matches found!")
        return

    if matches['character_matches']:
        print("\nCharacter Matches (enter 'c1' for first character match, 'c2' for second, etc.):")
        for i, match in enumerate(matches['character_matches'], 1):
            print(f"c{i}. {match['character']}: {match['count']} cards with numbers {match['numbers']}")
    
    if matches['number_matches']:
        print("\nNumber Matches (enter 'n1' for first number match, 'n2' for second, etc.):")
        for i, match in enumerate(matches['number_matches'], 1):
            print(f"n{i}. Number {match['number']}: {match['count']} cards with characters {match['characters']}")

def remove_set(player_hand, matches, discard_pile, choice):
    if not choice:
        return False
    
    match_type = choice[0]  # 'c' for character, 'n' for number
    try:
        match_index = int(choice[1]) - 1  # Convert to 0-based index
    except (ValueError, IndexError):
        print("Invalid choice!")
        return False

    cards_to_remove = []
    
    if match_type == 'c' and match_index < len(matches['character_matches']):
        # Remove character match
        match = matches['character_matches'][match_index]
        character = match['character']
        numbers = match['numbers'][:3]  # Take only first 3 if more exist
        
        for card in player_hand[:]:  # Create a copy to iterate over
            if card[0] == character and card[1] in numbers and len(numbers) > 0:
                cards_to_remove.append(card)
                numbers.remove(card[1])
                
    elif match_type == 'n' and match_index < len(matches['number_matches']):
        # Remove number match
        match = matches['number_matches'][match_index]
        number = match['number']
        characters = match['characters'][:3]  # Take only first 3 if more exist
        
        for card in player_hand[:]:  # Create a copy to iterate over
            if card[1] == number and card[0] in characters and len(characters) > 0:
                cards_to_remove.append(card)
                characters.remove(card[0])
    else:
        print("Invalid choice!")
        return False

    # Remove cards and add to discard pile
    for card in cards_to_remove:
        player_hand.remove(card)
        discard_pile.append(card)
    
    return True

def test_matching():
    # Example hand with some matches
    player_hand = [
        ("Blue Sorceress", 5),
        ("Blue Sorceress", 7),
        ("Blue Sorceress", 9),  # Character match (Blue Sorceress x3)
        ("Orange Rogue", 4),
        ("Purple Warrior", 4),
        ("Green Ranger", 4),    # Number match (4 x3)
        ("Orange Rogue", 7),
    ]
    
    discard_pile = []
    
    while True:
        print("\nPlayer's hand:")
        for card in player_hand:
            print(f"{card[0]}: {card[1]}")
            
        matches = find_matches(player_hand)
        if not matches['character_matches'] and not matches['number_matches']:
            print("\nNo more matches available!")
            break
            
        print_matches(matches)
        
        choice = input("\nEnter set to remove (e.g., 'c1' or 'n1'), or press Enter to stop: ").lower()
        if not choice:
            break
            
        if remove_set(player_hand, matches, discard_pile, choice):
            print("\nSet removed successfully!")
            print("Discard pile:", discard_pile)
        else:
            print("\nFailed to remove set. Please try again.")

if __name__ == "__main__":
    test_matching()