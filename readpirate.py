consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


to_pirate = str(input("Skriv din mening som ska översättas här: "))
outstring = ""
for char in to_pirate:
    if char in consonants:
        outstring += char+"o"+char
    else:
        outstring += char

print(outstring)

f = open('pirate.txt', 'r+')
f.write(outstring)

f.close()