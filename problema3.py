# Avand un cuvant x si un alfabet V sa se verifice daca x este cuvant peste V.

from culori import Culoare


def functie(x, V):
    for ch in x:
        # spatiul este lamda, deci trecem peste el
        if ch is ' ':
            continue
        # am folosit try si except deoarece index este o functie
        # de cautare ce returneaza ValueError in caz ca nu gaseste
        try:
            V.index(ch)
        except ValueError:
            return False
    return True


alfabet = 'tam'
cuvant = 'mama tata'

print('mama si tata', Culoare.blue if functie(cuvant, alfabet) else Culoare.red + 'nu', 'este')
