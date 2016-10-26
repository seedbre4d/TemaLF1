# Sa se verifice daca doua cuvinte citite de la tastatura rimeaza
# (spunem ca doua cuvinte rimeaza daca ultimele doua caractere sunt identice).

from culori import Culoare


def rhymes(w1, w2):
    #        ultimele 2 caract ale w1   ultimele 2 caract ale w2
    return True if (w1[len(w1) - 2:] == w2[len(w2) - 2:]) else False


w1 = input()
w2 = input()
print(w1, "si", w2, Culoare.blue + "rimeaza" if rhymes(w1, w2)else Culoare.red + "nu rimeaza")
