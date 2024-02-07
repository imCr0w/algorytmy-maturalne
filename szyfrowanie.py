test=""
#funkcje do cezara czyli przesuwanie liter o ileś miejsc
def cezarCry(word,key):
    key%=26
    odp=""
    for i in word:
        if ord(i)>=97 and ord(i)+key>122:
            odp+=chr(96+(ord(i)+key-122))
        elif ord(i)>64 and ord(i)+key>90:
            odp+=chr(64+(ord(i)+key-90))
        else:
            odp+=chr(ord(i)+key)
    return odp

def cezarDe(pw,key):
    key%=26
    odp=""
    for i in pw:
        if ord(i)>=97 and ord(i)-key<97:
            odp+=chr(123-(97-(ord(i)-key)))
        elif ord(i)>64 and ord(i)-key<65:
            odp+=chr(91-(65-(ord(i)-key)))
        else:
            odp+=chr(ord(i)-key)
    return odp
#zamienia lietery kolejnosci w parach
def przestawienie(word):
    odp=""
    for i in range(0,len(word),2):
        if i+1<len(word):
            odp+=word[i+1]
        odp+=word[i]
    return odp
#szyfr płotkowy, robisz taki jakby płotek i potem czytasz wartosci z danego poziomu plotka, płotek idzie w taki sposob, (hasło to ABCDEFG, a wynik to bedzie AEBDFCG
#A        E
#  B    D    F
#    C          G
#daje algo do robienia plotka i deszyfrowania go, jest inna opcja szyfrowania i robisz po prostu prostokąt z pustych miejsc w tabeli dwuwymiarowej o dlugosci slowa i wysokosci ilosci poziomow i dajesz po kolei 
#wartosci w odpowiednie miejsca a potem zczytujesz rzedami, moje podejscie jest bardziej pracyzyjne
def enPlotek(word,level):
    odp=""
    tab=[[]for i in range(level)]
    poziom=0
    zmieniacz=1
    for j in word:
        tab[poziom]+=j
        poziom+=zmieniacz
        if poziom==level-1:
            zmieniacz=-1
        if poziom==0:
            zmieniacz=1
    for i in tab:
        for j in i:
            odp+=j
    return odp
#ten kod oblicza ile jest znakow w danym poziomie i zwraca tablice z tymi wartosciami, np jesli slowo ma dlugosc 8 to na pierwszym poziomie beda 2 litery, na 2 4 a na 3 2, wiec wynik to 2,4,2
#jest to potrzebne w deszyfrowaniu, zeby bylo wiadomo ile znakow z otrzymanego szyfrogramu pryzpisac do danej tablicy w matrycy czyli danego poziomu w płotku
def obliczSek(dlug,level):
    tab=[0 for i in range(level)]
    poziom=0
    zmieniacz=1
    for i in range(dlug):
        tab[poziom]+=1
        poziom+=zmieniacz
        if poziom==0:
            zmieniacz=1
        if poziom==level-1:
            zmieniacz=-1
    return tab

def dePlotek(word,level):
    tab=[[]for j in range(level)]
    sek=obliczSek(len(word),level)
    poziom=0
    print(sek)
    index=0
    for j in range(level):
        for i in range(sek[poziom]):
            tab[j]+=word[index]
            index+=1
        poziom+=1
    odp=""
    poziom=0
    zmieniacz=1
    for i in range(len(word)):
        odp+=tab[poziom][0]
        tab[poziom].pop(0)
        poziom+=zmieniacz
        if poziom==0:
            zmieniacz=1
        if poziom==level-1:
            zmieniacz=-1
    return odp
#nazywa sie vigenere, ale vinegre jakoś milej wchodzi, niby trzeba robić cała tablice do tego wielkości 25^2, ale jak zobaczysz tablice to ogarniesz jak ona dziala i nie bedzie ptrzeby robienia jej, ogolnie masz swoje haslo i masz klucz
# i do pierwszej litry hasla dodajes pierwsza litere klucza, do drugiej drugą itd, jesli skonczy ci sie klucz to lecisz od początku, ten kod zakłada, że wszystko było w capslocku, możesz użyć .lower() lub .upper(), żeny sprowadizć do swoich literek
#obliczasz pozycje litery w alfabecie odejmując ASCII litery A, bo w oryginalenj tablicy A oznaczało 0
def enVinegre(word,key):
    odp=""
    for i in range(len(word)):
        keyVal=ord(key[i%len(key)])-65
        new=ord(word[i])+keyVal
        if new>90:
            new-=26
        odp+=chr(new)
    return odp

def deVinegre(word,key):
    odp=""
    for i in range(len(word)):
        keyVal=ord(key[i%len(key)])-65
        new=ord(word[i])-keyVal
        if new <65:
            new+=26
        odp+=chr(new)
    return odp
#oh man, fairplay jest mega fajne i finalnei proste do zrobienia, nie spoileruję, miłej zabawy,polecm zrobienie sobie osobnych funkcji na różne zadania, jak piszesz kod możesz je testować na żywo i łatwij zobaczysz co idzie nie tak w kodzie
def Filler(tab):
    banLista=[]
    for i in tab:
        for j in i:
            banLista.append(j)
    if 'j' not in banLista:
        banLista.append('j')
    elif 'x' not in banLista:
        banLista.append('x')
    elif 'q' not in banLista:
        banLista.append('q')
    alfabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for rzad in range(5):
        for kol in range(5):
            if tab[rzad][kol]=="":
                while tab[rzad][kol]=="":
                    if alfabet[0] not in banLista:
                        tab[rzad][kol]=alfabet[0]
                        alfabet.pop(0)
                    else:
                        alfabet.pop(0)

def keyCreator(key):
    key=key.lower()
    tab=[[""for i in range(5)] for j in range(5)]
    keyChar=[]
    for i in key:
        if i not in keyChar:
            keyChar.append(i)
    rzad=0
    kol=0
    for i in keyChar:
        tab[rzad][kol]=i
        kol+=1
        if kol==5:
            rzad+=1
            kol=0
    Filler(tab)
    return tab

def szukaj(tab,ele):
    for i in range(5):
        for j in range(5):
            if tab[i][j]==ele:
                return i,j

def enFairplay(word,key):  
    keyTab=keyCreator(key)  
    print(keyTab)  
    kon=''  
    if len(word)%2==1:  
        kon=word[len(word)-1]  
        word=word[:len(word)-1]  
    odp=""  
    for i in range(0,len(word),2):  
        char1=word[i]  
        char2=word[i+1]  
        r1,k1 = szukaj(keyTab,char1)  
        r2,k2 = szukaj(keyTab,char2)  
        if r1==r2:  
            odp+=keyTab[r1][(k1+1)%5]  
            odp+=keyTab[r2][(k2+1)%5]  
        elif k1==k2:  
            odp+=keyTab[(r1+1)%5][k1]  
            odp+=keyTab[(r2+1)%5][k2]  
        else:  
            odp+=keyTab[r2][k1]  
            odp+=keyTab[r1][k2]  
    if kon!='':  
        odp+=kon  
    return odp
    
def deFairplay(word,table):  
    odp=""  
    kon=""  
    if len(word)%2==1:  
        kon=word[len(word)-1]  
        word=word[:len(word)-1]  
    for index in range(0,len(word),2):  
        char1=word[index]  
        char2=word[index+1]  
        r1,k1=szukaj(table,char1)  
        r2,k2=szukaj(table,char2)  
        if r1==r2:  
            odp+=table[r1][(k1-1)%5]  
            odp+=table[r2][(k2-1)%5]  
        elif k1==k2:  
            odp+=table[(r1-1)%5][k1]  
            odp+=table[(r2-1)%5][k2]  
        else:  
            odp+=table[r2][k1]  
            odp+=table[r1][k2]  
    if kon!= "":  
        odp+=kon  
    return odp
#tutaj tłumacze z laciny na morsea i w druga strone, pierwsza funkcja sprawia, ze nie musze recznie robić tej długiej listyw drugiej funkcji tylko mam miłą pomoc
def morsListCreator():
    tab=[[chr(97+i) for i in range(26)]for j in range(2)]
    for index in range(26):
        print(tab[0][index])
        tab[1][index]=input("podaj znak: ")
    print(tab)

def morsTrans(char,type):
    tab=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], ['*-', '-***', '-*-*', '-**', '*', '**-*', '--*', '****', '**', '*---', '-*-', '*-**', '--', '-*', '---', '*--*', '--*-', '*-*', '***', '-', '**-', '***-', '*--', '-**-', '-*--', '--**']]
    if type=='e':
        char=char.lower()
        for index in range(26):
            if tab[0][index]==char:
                return tab[1][index]
    elif type=='d':
        for index in range(26):
            if tab[1][index]==char:
                return tab[0][index]
    else:
        print("zły rodzaj, wybierz e dla szyfrowania albo d dla deszyfrowania")

def enMors(text):
    odp=""
    for i in text:
        odp+=morsTrans(i,'e')
    return odp

#ponieważ nie było podanej formy, zakładam, że odszyfrujemy tabelę ze znakami morsa
#jesli msz stringa ogarnij jak oddzielone sa poszczegolne znaki, bez tego string bedzie nieczytelny
def deMors(znaki):
    odp=""
    for i in znaki:
        odp+=morsTrans(i,'d')
    return odp
#tu jest szyfr którego dostałem opis na zajeciach i musiałem zrobić ale on jest w miare popularny, masz haslo i masz klucz, klucz to dwie cyfry, ilosc kolumn i przesuniecie, wkladasz haslo swoje do tabelki bez spacji,
#potem przesuwasz litery o podana wartosc w rzedach a potem czytasz w kolumnach od goy do dołu, czyli
#"ala ma kota" key 32
# A  L  A       L  A  A 
# M  A  K   --> A  K  M --> LATAKAAMO
# O  T  A       T  A  O
def tabelkowanie(text,kod):
    text=text.replace(" ","")
    kol=kod//10
    rze=len(text)/kol
    if(rze!=len(text)//kol):
        rze+=1
    tab=[[""for i in range(kol)]for j in range(int(rze))]
    k=0
    r=0
    for i in text:
        tab[r][k]=i
        k+=1
        if k == kol:
            r+=1
            k=0
    return tab, rze

def szyfr(text,kod):
    przes=kod%10
    kol=kod//10
    tab, rz=tabelkowanie(text,kod)
    przes%=kol
    odp=[]
    for i in tab:
        newTab=["" for j in range(kol)]
        for index in range(kol):
            newTab[(index+przes)%kol]=i[index]
        odp.append(newTab)
    odpText=""
    for k in range(kol):
        for r in range(int(rz)):
            odpText+=odp[r][k]
    return odpText

def deszyfr(text,kod):
    przes = kod % 10
    kol = kod // 10
    rz = len(text)/kol
    if rz!= int(rz):
        rz+=1
        rz=int(rz)
    przes %= kol
    ogTab=[[""for i in range(kol)]for j in range(int(rz))]
    index=0
    while index<len(text):
        for k in range(kol):
            for r in range(int(rz)):
                ogTab[r][k]=text[index]
                index+=1
    odpTab=[]
    for i in ogTab:
        new=[""for i in range(kol)]
        for index in range(kol):
            new[(index - przes) % kol] = i[index]
        odpTab.append(new)
    odp=""
    for i in odpTab:
        for j in i:
            odp+=j
    return odp
