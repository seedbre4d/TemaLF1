# Sa se determine daca un sir de caractere contine un anumit caracter dat.
# Sa se determine de cate ori apare caracterul in sir.
from culori import Culoare


def functie(string, ch):
    times = 0
    for let in string:
        if ch is let:
            times += 1
    return times


print("Sir de caracteresd: ")
string = input()
while True:
    print("Caracter de cautat: ", end='')
    ch = input()
    if len(ch) == 1:
        break
    print("Trebuie introdus un singur caracter. Mai incearca o data.")
if functie(string, ch) > 0:
    print("Caracterul {}{} apare {}de {} ori in {}".format(ch, Culoare.blue, Culoare.default, functie(string, ch),
                                                           string))
else:
    print("Caracterul {}{} nu apare {}in {}".format(ch, Culoare.red, Culoare.default, string))
