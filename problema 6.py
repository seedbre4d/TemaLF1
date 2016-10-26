'''

 Scrieti un subprogram prin care se citesc n cuvinte de la tastatura.

-sa se sorteze cuvintele in ordine crescatoare
-sa se afiseze in ordine inversa citirii toate cuvintele (recursivitate,
fara vector de  cuvinte - !cuvintele in sine nu se inverseaza!)

'''


def citire_p1(n: int):
    word_list = []
    for i in range(n):
        word_list.append(input())
    return word_list


def citire_p2(word_list, n):
    word_list.append(input())
    if n > 1:
        citire_p2(word_list, n - 1)
    print(word_list[n - 1])


print("Marime: ", end='')
n = int(input())

print("     Prima parte ")
word_list = citire_p1(n)
word_list = sorted(word_list)
print(word_list, '\n\n')
print("     A doua parte")

citire_p2([], n)
