'''

 Scrieti un subprogram prin care se citesc n cuvinte de la tastatura.

-sa se sorteze cuvintele in ordine crescatoare
-sa se afiseze in ordine inversa citirii toate cuvintele (recursivitate,
fara vector de  cuvinte - !cuvintele in sine nu se inverseaza!)

'''


# a doua parte n-am inteles-o

def citire(n: int):
    wordlist = []
    for i in range(n):
        wordlist.append(input())
    return wordlist


wordlist = citire(4)
wordlist = sorted(wordlist)

print(wordlist)
