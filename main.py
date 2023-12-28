def read_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents 

def count_words(text):
    splited = text.split()
    return len(splited)

def count_letters(text):
    letters_dict = dict()
    for s in text:
        if s.isalpha():
            lowered = s.lower()
            letter_in_dict = letters_dict.get(lowered, None) 
            if letter_in_dict == None:
                letters_dict[lowered] = 1 
            else:
                letters_dict[lowered] = letters_dict[lowered] + 1 

    return letters_dict

def get_sort_key(a):
    return a[1]

def main():
    print("====================== Begin report for Frankenstein Book ===========================")
    content = read_content()
    word_count = count_words(content)
    print(f"Book word count is {word_count}")
    letter_count = count_letters(content)
    letters_list = list(letter_count.items())
    letters_list.sort(key=get_sort_key, reverse=True)
    for row in letters_list:
        print(f"The {row[0]} character appers {row[1]} times.")
    print("========================= Finished =========================")

main()
