
def count_words(text: str) -> int:
    words = text.split()
    # print(words)
    return len(words)

def count_char(text):
    found: dict = {} 
    
    for c in text.lower():
        if c.isalpha():
            if found.get(c):
                found[c] += 1
            else:
                found[c] = 1
    return found

def sort_on(items):
    return items["num"]           

def sort_char(found:dict):
    dict_list = []

    for k in found:
        dict_list.append({'char': k, 'num': found[k]})


    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
    



