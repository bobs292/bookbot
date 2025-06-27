def get_num_words(text):
    return len(text.split())

def get_count_Letters(text):
    text = text.lower()
    my_dict = {}
    for char in text:
        if not char.isspace():
            if char in my_dict:
                my_dict[char] += 1
            else: 
                my_dict[char] = 1
    return my_dict

def sort(dicta):
    sorted_by_values = dict(sorted(dicta.items(), key=lambda item: item[1], reverse=True))
    return sorted_by_values

