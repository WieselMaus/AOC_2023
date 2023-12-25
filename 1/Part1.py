with open("input", "r") as f:
    f = f.read()

f = f.replace("three","th3ree").replace("eight","ei8ght").replace("two","t2wo").replace("one","on1e")\
    .replace("nine","n9ine").replace("seven","seve7n").replace("six","si6x").replace("four","fo4ur").replace("five","fiv5e")
print(f)
f = f.splitlines()
Ergebnis = 0

for line in f:
    Zettel = []
    for buchstabe in line:
        # ist buchstabe eine zahl?

        if buchstabe.isdigit():
            Zettel.append(buchstabe)
    Vorne = int(Zettel[0])
    Hinten = int(Zettel[-1])
    Vorne *= 10
    Linie = Vorne + Hinten
    print(Linie)
    Ergebnis += Linie
print(Ergebnis)
