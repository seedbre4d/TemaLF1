# Sa se inverseze un sir de caractere si apoi sa se inlocuiasca toate aparitiile subsirului SA cu aaa.
from culori import Culoare


def functie(string: str):
    newstring = string[::-1]  # newstring este string inversat
    # am folosit try si except deoarece index este o functie
    # de cautare ce returneaza ValueError in caz ca nu gaseste
    try:
        newstring.index('SA')
    except ValueError:
        return "Nu am gasit SA."
    # returneaza rezultatul sub forma <text_inainte_de_SA>.albastru.fff/a<text_dupa_SA>
    return newstring[0:newstring.index("SA")] + culoare.blue + 'aaa' + culoare.default + newstring[
                                                                                         newstring.index("SA") + \
                                                                                         len("SA"):]


string = "ab c def g arASk mer"
print(functie(string))
