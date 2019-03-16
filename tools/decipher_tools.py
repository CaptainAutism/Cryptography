from collections import Counter
from tools.converter_tools import Converter


def letter_frequencies(text):
    len_text = len(text)
    counts = Counter(text)
    freqs = {letter: counts[letter]/len_text for letter in counts}
    print(freqs)
    print(f"Max letter freq is {max(freqs)} with frequency {freqs[max(freqs)]}")
    return freqs


def possible_shift_ciphers(text):
    converter = Converter()
    possible_codes = [converter.shift_text(text, i) for i in range(26)]
    return possible_codes

