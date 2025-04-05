def word_count(text):
    num_words = len(text.split())
    return num_words

def character_count(text):
    counts = {}
    for c in text:
        lowered_c = c.lower()
        if lowered_c in counts:
            counts[lowered_c] += 1
        else:
            counts[lowered_c] = 1
    return counts

def sorted_list(dict):
    fancy_list = []
    for i in dict:
        fancy_list.append({"char": i, "count": dict[i]})
    fancy_list.sort(reverse=True, key=sort_on)
    return fancy_list

def sort_on(dict):
    return dict["count"]
