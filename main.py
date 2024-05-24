def num_words(text):
    return len(text.split())

def get_chars_dict(text):
    unified_text = text.lower()
    all_chars = {}
    for char in unified_text:
        if char not in all_chars:
            all_chars[char] = 1
        else:
            all_chars[char] = all_chars[char] + 1
    return all_chars

def get_list_chars_dicts(chars_dict):
    list = []
    for char in chars_dict:
        list.append({"char": char, "num": chars_dict[char]})
    return list

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankstein.txt") as f:
        text = f.read()
        words = num_words(text)
        chars_dict = get_chars_dict(text)
        list_chars_dicts = get_list_chars_dicts(chars_dict)

        list_chars_dicts.sort(reverse=True, key=sort_on)

        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")

        for char_stat in list_chars_dicts:
            if char_stat["char"].isalpha():
                print(f"The '{char_stat["char"]}' character was found {char_stat["num"]} times")

        print("--- End report ---")
        

main()