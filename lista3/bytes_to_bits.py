byte_lines = []
lines = []
byte_line = ''
filepath_salsa = 'data1char.txt'
filepath_sam = 'data2char.txt'
salsa_out = 'data1.txt'
sam_out = 'data2.txt'


with open(filepath_salsa) as fp:
    for cnt, line in enumerate(fp):
        byte_line = ''
        for character in line:
            byte_line = byte_line + '{0:08b}'.format(ord(character)) + ''
        byte_lines.append(byte_line)

with open(salsa_out, "w") as ofp:
    for line in byte_lines:
        i = 1
        for character in line:
            ofp.write(character)
            if i%8 == 0:
                ofp.write(" ")
            i+=1
        ofp.write("\n")


