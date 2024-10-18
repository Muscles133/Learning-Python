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
    
    # Find matches (3)
    matches = {
        'character_matches': [],
        'number_matches': []
    }
    
    # Check for character matches (same character, different numbers)
    for character, numbers in character_counts.items():
        if len(numbers) == 3:
            matches['character_matches'].append({
                'character': character,
                'count': len(numbers),
                'numbers': sorted(numbers)
            })
    
    # Check for number matches (same number, different characters)
    for number, characters in number_counts.items():
        if len(characters) == 3:
            matches['number_matches'].append({
                'number': number,
                'count': len(characters),
                'characters': sorted(characters)
            })
    
    return matches

def print_matches(matches):
    if not matches['character_matches'] and not matches['number_matches']:
        return "No matches found!"

    if matches['character_matches']:
        print("You have a SCREAM!")
    
    if matches['number_matches']:
        print ("You have a STOMP!")


def main():
    player_hand = [
        ("Blue Sorceress", 5),
        ("Blue Sorceress", 7),
        ("Blue Sorceress", 9),  # Character match (Blue Sorceress x3)
        ("Orange Rogue", 4),
        ("Purple Warrior", 4),
        ("Green Ranger", 4),    # Number match (4 x3)
        ("Orange Rogue", 7),
    ]

    matches = find_matches(player_hand)
   
    print_matches(matches)




if __name__ == "__main__":
    main()