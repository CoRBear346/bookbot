


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def word_count(filepath):
    text = get_book_text(filepath)
    return len(text.split())

def character_count(filepath):
    characters = list(get_book_text(filepath))
    character_dict = {}
    for character in characters:
        character = character.lower()
        if character in character_dict:
             character_dict[character.lower()] += 1
        else:
             character_dict[character.lower()] = 1
    return character_dict

def sort_key(items):
    return items["count"]

def character_sort(character_dict):
    dict_list = []
    for character, count in character_dict.items():
        pair_dict = {}
        pair_dict["character"] = character
        pair_dict["count"] = count
        dict_list.append(pair_dict)
    dict_list.sort(reverse=True, key=sort_key)
    return dict_list

def report_maker(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(filepath)} total words")
    print("--------- Character Count -------")

    for value in character_sort(character_count(filepath)):
        if value["character"].isalpha():
            print(f"{value['character']}: {value['count']}")
    print("============= END ===============")

