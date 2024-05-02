def load_words(file_path):
    """Load words from a given file into a set."""
    with open(file_path, 'r') as file:
        return {line.strip() for line in file if line.strip()}


def find_valid_words(words, key_letter, supplementary_letters):
    """Find valid words based on Spelling Bee rules."""
    all_letters = set(supplementary_letters.lower()) | {key_letter.lower()}
    valid_words = {
        word for word in words
        if len(word) >= 4
        and key_letter.lower() in word
        and set(word).issubset(all_letters)
        and word.islower()
    }
    return valid_words


def main():
    file_path = r"C:\Users\tmwil\OneDrive\Desktop\Spelling Bee\words_alpha.txt"
    key_letter = 'X'  # Example key letter
    supplementary_letters = 'SRETIG'  # Example supplementary letters

    words = load_words(file_path)
    valid_words = find_valid_words(words, key_letter, supplementary_letters)

    for word in sorted(valid_words):
        print(word)


if __name__ == '__main__':
    main()
