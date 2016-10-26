# Sa se inverseze un sir de caractere si apoi sa se inlocuiasca toate aparitiile subsirului SA cu aaa.
from culori import Culoare


def functie(string: str):
    new_string = string[::-1]  # new_string este string inversat
    # am folosit try si except deoarece index este o functie
    # de cautare ce returneaza ValueError in caz ca nu gaseste
    try:
        new_string.index('SA')
    except ValueError:
        return "Nu am gasit SA."
    # returneaza rezultatul sub forma <text_inainte_de_SA>.albastru.fff/a<text_dupa_SA>
    return new_string[0:new_string.index("SA")] + Culoare.blue + 'aaa' + Culoare.default + new_string[
                                                                                         new_string.index("SA") + \
                                                                                         len("SA"):]


string = "ab c def g arASk mer"
print(functie(string))
