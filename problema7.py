#  Sa se scrie o functie care sa returneze lungimea unui sir de caractere, transmis ca parametru.

def lungime(string: str):
    length = 0
    for i in string:
        length += 1
    return length


print(lungime("abcd"))
