# Sa se determine daca un sir de caractere este un numar natural, intreg sau real.


def functie(a: str):
    if a.isdigit():
        # daca toate char-urile sunt cifre, e clar natural
        return "Natural"
    if a[0] == '-' and a[1:].isdigit():
        # daca primul char este - iar urmatoarele sunt cifre, e clar intreg
        return "Intreg"
    try:
        # daca niciunul din cazurile de mai sus nu se aplica
        # si nu il gasesc nici pe . e clar ca avem char intrus
        # am folosit try si except deoarece functia index returneaza
        # ValueError daca nu este gasit caracterul cautat
        a.index('.')
    except ValueError:
        return "Not a number"
    if a[1:a.index('.') - 1].isdigit() and a[a.index('.') + 1:].isdigit():
        # verificam daca este numar in spatele si dupa punct
        if not a[0].isdigit() and a[0] is not '-':
            return "Not a number"
        return "Real"

    return "Not a number"


print(functie("231"), functie("-23123"), functie("-2312.321223"))
