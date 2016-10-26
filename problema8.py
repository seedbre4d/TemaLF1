# Sa se afiseze unul sub altul, toate prefixele proprii ale unui cuvant citit de la tastatura
# (prefixele unui cuvant sunt compuse din minim un caracter si maxim toate caracterele,
# citite de la stanga la dreapta).


def prefixe_proprii(word: str):
    for ch in range(len(word) + 1):
        print(word[0:ch])


word = input()
prefixe_proprii(word)
