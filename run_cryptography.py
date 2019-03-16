from tools.decipher_tools import *
from tools.file_tools import *

common_words = ["the", "and", "with", "for", "so", "at", "can", "have", "with", "but", "from", "with", "have"]

if __name__ == "__main__":
    raw_text = get_text('text_file.txt')
    text = clean_text(raw_text)
    freqs = letter_frequencies(text)

    list_of_possible_shift_decodes = possible_shift_ciphers(text)
    list_of_possible_multiply_decodes = possible_multiplicative_ciphers(text)

    all_deciphers = list_of_possible_shift_decodes + list_of_possible_multiply_decodes

    for decipher in all_deciphers:
        count = 0
        for word in common_words:
            if word in decipher:
                count += decipher.count(word)
        if count > 4:
            print(decipher+'\n\n')


