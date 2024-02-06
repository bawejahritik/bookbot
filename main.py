def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = 1 + freq.get(char.lower(), 0)
    return freq

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        num_of_words = count_words(text)
        print("--- Begin report of books/frankenstein.txt ---")
        
        print(f"{num_of_words} words found in the document")
        num_of_letters = count_letters(text)    
        letters = []
        for letter, count in num_of_letters.items():
            letters.append({"letter": letter, "num":count})

        letters.sort(reverse=True, key=sort_on)

        for pair in letters:
            letter = pair["letter"]
            count = pair["num"]
            print(f"The '{letter}' was found {count} times")

        print("--- End report ---")

if __name__ == '__main__':
    main()