import numpy as np
test=[4,3,1,2,5,1]
testABC=['A','C','B','T','Z','A']
testeMAT=[[4,2,3,4],[45,3,2,6],[3,23,53,17],[36,28,3,5]]
testKurs=[[4,5,6,4],[3,3,2,7],[1,1,1,1]]

#ogólnie jest fajny kanał na yt który pokazuje różne sortowanie, imo bardzo ciekawe i fajnie się ogląda i dobrze tłumaczy zasady działania każdego alorytmu, niżej daje link do kanału
#https://www.youtube.com/@udiprod

#sortowanie bąbelkowe, pretty basic, dla każdego elementu przesuwaz go tak wysoko jak się da, tyle iteracji ile elementów
def bubbleSort(tab):
    dlug=len(tab)
    for i in range(0,dlug):
        for j in range(1,dlug):
            if tab[j-1] > tab[j]:
                mn=tab[j]
                tab[j]=tab[j-1]
                tab[j-1]=mn
    return tab

#sortowanie przez wybor po polsu czy jakoś tak, szukasz najmniejszej wartosci i układasz je po kolei, czyi najpierwsz szuaksz najmniejszej wartosci dla indexu 0, potem najemnijeszej dla indexu 1 itp itd, pamietaj zeby iterowac
#indexu dla ktorego szukasz obecnie najmniejszej wartości
def selectionSort(tab):
    for i in range(0,len(tab)-1):
        najm=tab[i]
        najmIndex=i
        for j in range(i,len(tab)):
            if najm>tab[j]:
                najm=tab[j]
                najmIndex=j
        tab[najmIndex]=tab[i]
        tab[i]=najm

#sortowanie rekur, średnio przyjemny temat, ale czasem trzeba, ogólnie dzielisz swoją tablicę na pół dopóki nie dotrzesz do tablic o rozmiarze 1, potem bierzesz dwie tablice, iterujesz je od lewej do prawej i do nowej tablicy dajesz 
#mniejszą wartość, czyli najpierw porównujesz 1 wartosc z lewej i pierwsza z prawej tablicy (prawa i lewa wziela sie z tego, że wczesniej podzieliliśy tablicę na 2 części) i do nowej tablicy dodajesz te mniejsza ( załóżmy że mniejsza wartość
# była z lewej strony, teraz porownujesz 2 wartośc z lewej i 1 z prawej i tak aż ci się skońcżwartości, potem dla pewnosci dodajesz to co zostało w danych tablicach, ja tutaj zrobiłem risky move, nie tworzyłem nowej tablicy, ale działa
def mergeSort(tab):
    if len(tab)>1:
        mid=len(tab)//2
        L=tab[:mid]
        R=tab[mid:]
        mergeSort(L)
        mergeSort(R)

        lewy=prawy=ogolny=0
        while lewy<len(L) and prawy < len(R):
            if R[prawy]<=L[lewy]:
                tab[ogolny]=R[prawy]
                prawy+=1
            else:
                tab[ogolny] = L[lewy]
                lewy+=1
            ogolny+=1
        while lewy<len(L):
            tab[ogolny]=L[lewy]
            lewy+=1
            ogolny+=1
        while prawy<len(R):
            tab[ogolny]=R[prawy]
            prawy+=1
            ogolny+=1
# tutaj jest merge sort jak ma się tabele 2 wymiarową i trzeba posortować kolumny
def mergeMat(mat):
    odp=[]
    newmat=np.transpose(mat)
    print("trans matryca")
    print(newmat)
    for i in newmat:
        print("i")
        print(i)
        newi=mergeSort(i)
        print(newi)
        odp.append(i)
    print("odp najpierw")
    print(odp)
    newodp=np.transpose(odp)
    print("odp po")
    print(newodp)

testQuick=[8,1,2,3,7,8,2,1,4]

#ogólnie bierzesz sobie pivota, czyli taki punkt odniesienia, i ustawiasż granicę na samym początku tablicy, przed pierwsza wartością, jeśli wartość jest mniejsza niż pivot, przesuwasz wartość za granicę, jak przeiterujesz cała tabelę, 
#dajesz pivota na koniec granicy, to jest teraz twójpewniak, czyli wartość która na pewno jest w dobrym miejscu w tabeli, bo wszytskie wartości mniejsze od niej są przed nią czyli za granicą, a wszystkie wieksze sa przed nia, decyzje,
#decyzje co zrobisz z tymi równymi pivotovi zostawiam tobie , dzielisz potem te tabele na dwie czesci, przed pewniakiem i po pewniaku, pamietaj ze nie moga one zawierac pewniaka i robisz dla nich to samo. az dojdziesz do tablicy wielkosci 1
#potem sklejasz lewa strone z pivotem a potem z prawa strona i oddajesz
def quickSort(tab):
    if len(tab)>1:
        granica=-1
        pivot=tab[len(tab)-1]
        obecne=0
        while obecne<(len(tab)):
            if tab[obecne]<pivot:
                temp=tab[granica+1]
                tab[granica+1]=tab[obecne]
                tab[obecne]=temp
                granica+=1
            obecne+=1
        tab[len(tab)-1]=tab[granica+1]
        tab[granica+1]=pivot
        pewniak=granica+1
        L=tab[:pewniak]
        R=tab[pewniak+1:]
        L=quickSort(L)
        R=quickSort(R)
        L.append(tab[pewniak])
        return L + R
    return tab

#bierzesz wartość i szukasz wstecz gdzie ja wlozyc miedzy mniejsze a wieksze
insTest=[8,5,7,2,3,5,2]
def insertionSort(tab):
    for obecne in range(1,len(tab)):
        i=obecne-1
        while i>=0 and tab[obecne]<=tab[i]:
            temp=tab[obecne]
            tab[obecne]=tab[i]
            tab[i]=temp
            i-=1
            obecne-=1
    return tab
