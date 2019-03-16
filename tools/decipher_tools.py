from collections import Counter
from tools.converter_tools import Converter
from models.frequencies import Frequencies


def letter_frequencies(text):
    len_text = len(text)
    counts = Counter(text)
    freqs = [Frequencies(letter, counts[letter]/len_text) for letter in counts]
    sorted_freqs = sorted(freqs, key=lambda frequency: frequency.freq, reverse=True)
    print(sorted_freqs)
    print(f"Max letter freq is {sorted_freqs[0].letter} with frequency {sorted_freqs[1].freq}")
    return freqs


def possible_shift_ciphers(text):
    converter = Converter()
    possible_codes = [converter.shift_text(text, i) for i in range(26)]
    return possible_codes


def possible_multiplicative_ciphers(text):
    converter = Converter()
    valid_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    possible_codes = [converter.shift_text(text, i) for i in valid_values]
    return possible_codes
