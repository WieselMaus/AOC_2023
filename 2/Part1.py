with open("inputtest", "r") as f:
    f = f.read()
f = f.splitlines()
Zettel = 0
for line in f:
    line = line.split(";")
    for digit in line:
        digit = digit.split(",")
        for part in digit:
            part = part.split(" ")
            print(part)