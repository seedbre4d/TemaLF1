'''

Determinati numarul de cuvinte dintr-o fraza introdusa de  la tastatura,
precum si ce cuvinte sunt in fraza respectiva,sub forma:

 ex: "Ce cuvinte sunt in fraza? Determina!!"

 1. Ce
 2. cuvinte
 3. sunt
 4. in
 5. fraza
 6. Determina

 Ignorati , . ? ! ...

'''


def functie(string: str):
    count = 0  # count pt. nr din fata cuvantului
    word = ''  # intitial string-ul de printat este gol
    for ch in string:
        # daca un caracter face parte din alfabet, il
        # adaugam la cuvantul ce trebuie afisat
        if ch.isalpha():
            word += ch
        else:
            # daca nu face parte din alfabet, inseamna ca
            # putem afisa cuvantul gasit
            if len(word) > 0:
                count += 1
                print(str(count) + '. ' + word)
            word = ''  # dupa ce am afisat string-ul, il regolim pentru a fi reutilizat
    return None


string = "Ce cuvinte sunt in fraza? Determina!!"
functie(string)
