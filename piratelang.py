consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

to_pirate = str(input("Skriv din mening som ska översättas här: "))
output = ""
for char in to_pirate:
    if char in consonants:
        output += char + "o" + char
    else:
        output += char


f = open('pirate.txt', 'r+')
f.write(output)

f.close()
