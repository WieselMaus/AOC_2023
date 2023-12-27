with open("input", "r") as f:
    f = f.read()
f = f.splitlines()
Zettel = 0
max_green = 13
max_blue = 14
max_red = 12
Game = 0
for line in f:
    Game +=1
    line = line.split(":")[1]
    line = line.split(";")
    impossible = False
    for part in line:
        part = part.split(",")
        for p in part:
            p = p.strip()
            x = p.split(" ")[0]
            print("x", x)
            x = int(x)
            if "green" in p:
                p = p.strip()
                x = p.split(" ")[0]
                print("x" ,x)
                x = int(x)

                if x > max_green:
                    impossible = True
            if "red" in p:

                if x > max_red:
                    impossible = True
            if "blue" in p:

                if x > max_blue:
                    impossible = True
    if impossible != True:
        Zettel += Game

print(Zettel)
