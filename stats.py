def word_counter(text): 
    return len(text.split())


def character_counter(text):
    text = text.lower()
    split_list = list(text)
    new_dict = {}
    for i in split_list:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1

    return new_dict

def sort_on(items):
    return items["num"]


def chars_dict_sorted(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
   