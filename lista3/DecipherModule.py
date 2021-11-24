import operator


class DecipherModule:
    def __init__(self):
        self.ciphered = []
        self.deciphered = []
        self.letter_frequency = {
                                    'a':83, 'b':19, 'c':38, 'd':33, 'e':86, 'f':2,
                                    'g':14, 'h':12, 'i':88, 'j':22, 'k':30, 'l':22, 'm':28,
                                    'n':56, 'o':75, 'p':28, 'r':41, 's':41, 't':38, 'u':20,
                                    'w':41, 'x':0, 'y':40, 'z':53, 'v':0, 'q':1,
                                    'A': 18, 'B': 11, 'C': 13, 'D': 13, 'E': 18, 'F': 1,
                                    'G': 11, 'H': 11, 'I': 18, 'J': 12, 'K': 13, 'L': 12, 'M': 12,
                                    'N': 15, 'O': 17, 'P': 12, 'R': 14, 'S': 14, 'T': 13, 'U': 12,
                                    'W': 14, 'X': 0, 'Y': 4, 'Z': 5, 'V': 0, 'Q': 1,
                                    ' ': 100, '.':10, ',':11, '-': 6, '"': 7, '!': 5, '?': 5, ':': 4, ';': 3, '(': 5,')': 5,
                                    '0': 10, '1': 10, '2': 10, '3': 10, '4': 10, '5': 10, '6': 10, '7': 10, '8': 10, '9': 10
                                 }

    def add_cryptogram(self, data):
        chars = [chr(int(char, 2)) for char in str(data).strip().split(' ')]
        self.ciphered.append(chars)

    def find_possible_keybytes(self, position):
        keybytes = {}
        for cipher in self.ciphered:
            if len(cipher) <= position:
                continue
            for letter in self.letter_frequency.keys():
                keybyte = ord(cipher[position]) ^ ord(letter)
                keybytes[keybyte] = 0 + self.letter_frequency[letter] if keybyte not in keybytes.keys() else keybytes[keybyte] + self.letter_frequency[letter]
        keybytes = sorted(keybytes.items(), key=operator.itemgetter(1), reverse=True)
        return [k[0] for k in keybytes]

    def find_keystream(self):
        keystream = []
        max_length = 0
        for cipher in self.ciphered:
            max_length = max(max_length, len(cipher))

        for position in range(0, max_length):
            max_counter = 0
            best_keybyte = ' '
            keybytes = self.find_possible_keybytes(position)
            for keybyte in keybytes:
                counter = 0
                for cipher in self.ciphered:
                    if len(cipher) <= position:
                        continue
                    result = chr(ord(cipher[position]) ^ keybyte)
                    if result in self.letter_frequency.keys():
                        counter += 1
                if counter > max_counter:
                    max_counter = counter
                    best_keybyte = keybyte
            keystream.append(best_keybyte)
        return keystream

    def decipher(self):
        keystream = self.find_keystream()
        result = []
        for cipher in self.ciphered:
            index = 0
            for character in cipher:
                result.append(chr(ord(character) ^ keystream[index]))
                index += 1
            self.deciphered.append("".join(result))
            result = []


    def deciphered_by_index(self, index):
        return self.deciphered[index]

    def ciphered_by_index(self, index):
        return "".join(self.ciphered[index])

