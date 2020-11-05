import sys
from DecipherModule import DecipherModule


def main():
    i = 0
    decipher_module = DecipherModule()
    if len(sys.argv) > 1 :
        number_of_cryptograms = sys.argv[1]
    else:
        number_of_cryptograms = 21

    filepath = 'encrypted_data.txt'
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            decipher_module.add_cryptogram(line)
            i += 1
            if i >= number_of_cryptograms:
                break

    decipher_module.decipher()
    for index in range(number_of_cryptograms):
        print(decipher_module.deciphered_by_index(index), "\n")


main()
