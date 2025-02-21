def sort_on(dict):
    return dict["count"]

def print_report(word_count, char_counts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=sort_on)
    
    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")

def main():
    print("Starting report...") # Just keeping this one debug line
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()    
        word_count = len(file_contents.split())
    
    file_contents = file_contents.lower()
    character_counts = {}
    for char in file_contents:
        if char.isalpha():
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    
    print_report(word_count, character_counts)

main()