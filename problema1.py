# Sa se determine daca un sir de caractere contine un anumit caracter dat.
# Sa se determine de cate ori apare caracterul in sir.
from culori import Culoare


def functie(string, ch):
    times = 0
    for let in string:
        if ch is let:
            times += 1
    return times


print("Sir de caractere: ")
string = input()
while True:
    print("Caracter de cautat: ", end='')
    ch = input()
    if len(ch) == 1:
        break
    print("Trebuie introdus un singur caracter. Mai incearca o data.")
if functie(string, ch) > 0:
    print("Caracterul", ch, Culoare.blue + "apare" + Culoare.default, "de", functie(string, ch), "ori in", string)
else:
    print("Caracterul", ch, Culoare.red + "nu apare", Culoare.default + "in", string)
