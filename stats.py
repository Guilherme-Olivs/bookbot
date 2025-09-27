sort_par = 'num'

def _get_text(path):
    with open(path) as file:
        text = file.read()
    return text

def _get_sorting_key(items):
     return items[sort_par]

def get_num_words(file_path):
        text = _get_text(file_path)
        words = text.split()
        return len(words)
    


def get_num_char(file_path):
    buffer_text = _get_text(file_path)
    text = buffer_text.lower()
    char_counts = {}

    for c in text:
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1

    list_to_sort = [{'char': c, 'num': n} for c, n in char_counts.items()]
    
    list_to_sort.sort(reverse=True, key=_get_sorting_key)
    return list_to_sort
