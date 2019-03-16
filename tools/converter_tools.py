class Converter:
    def __init__(self):
        self._letter_to_num_conversion_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
                                               'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
                                               'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
                                               't': 20, 'u': 21, 'v': 22,'w': 23, 'x': 24, 'y': 25,
                                               'z': 0}
        self._num_to_letter_conversion_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
                                               10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
                                               18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
                                               0: 'z'}

    def letter_to_num(self, letter):
        return self._letter_to_num_conversion_dict[letter]

    def num_to_letter(self, num):
        return self._num_to_letter_conversion_dict[num]

    def shift_text(self, text, shift=0):
        result = ""
        for letter in text:
            num_repr = self.letter_to_num(letter)
            shifted = (num_repr + shift) % 26
            new_letter = self.num_to_letter(shifted)
            result += new_letter
        return result


