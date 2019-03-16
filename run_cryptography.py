from tools.decipher_tools import *
from tools.file_tools import *

if __name__ == "__main__":
    raw_text = get_text('text_file.txt')
    text = clean_text(raw_text)
    freqs = letter_frequencies(text)
    print(possible_shift_ciphers(text))

