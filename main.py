
def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    text = text.lower()  
    char_count = {}
    
    for char in text:
        if char.isalpha():  
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def print_report(file_contents):
    """Generate and print a report of word and character counts."""
    word_count = count_words(file_contents) 
    char_count = count_characters(file_contents)  

    
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

with open('books/frankenstein.txt', 'r') as f:
    file_contents = f.read()

print(file_contents)

print_report(file_contents)
