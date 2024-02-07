# NWD
def NWD (a,b):
    if a*b==0:
        return max(a,b)
    mniejsze = min(a,b)
    return NWD(mniejsze,max(a,b)%mniejsze)
def NWW (a,b):
    return (a*b)/NWD(a,b)
#przelicza z 10tnego na jaki chcesz
def dec2any(a,sys):
    if sys>10:
        if a<sys:
            if a>9:
                return chr(a+55)
            else:
                return str(a)
        else:
            if a%sys>9:
                return dec2any(int(a/sys),sys)+chr(a%sys +55)
            else:
                return dec2any(int(a/sys),sys)+str(a%sys)
    else:
        if a<sys:
            return a
        else:
            return dec2any(int(a / sys), sys) * 10 + a % sys

# z jakiego chcesz na 10
def any2dec(a,sys):
    if sys>10:
        poziom = len(a)
        if poziom==1:
            if ord(a)<60:
                return int(a)
            else:
                return ord(a)-55
        else:
            if ord(a[0])<60:
                return any2dec(a[1:],sys) + int(a[0])*(sys**(poziom-1))
            else:
                return any2dec(a[1:],sys) + (ord(a[0])-55)*(sys**(poziom-1))
    else:
        poziom = len(str(a))
        if poziom==1:
            return a
        else:
            return any2dec(a%(10**(poziom-1)),sys) + (int(a/(10**(poziom-1))))*(sys**(poziom-1))
#idk jaka doskonała liczba opisana w zadaniu
def czyDoskonala(liczba):
    sumaDzielników = 0
    for i in range(1,liczba):
        if(liczba%i==0):
            sumaDzielników+=i
    return sumaDzielników==liczba
#sprawdza to co mowi że sprawdza
def czyAnagram (pier, drugie):
    pierTab = []
    druTab = []
    for i in pier:
        pierTab.append(i)
    for i in drugie:
        druTab.append(i)
    pierTab.sort()
    druTab.sort()
    return pierTab==druTab
#tutaj chyba cos gadałem z nauczycielem i guess, mogłem się o coś kłócić, ale w dobrej wierze :D
def czyAnagram2(pier, drugie):
    #darujce te uppery, na filmiku z zalozenia wszystko bylo z duzych, tu sie tylko upewniam ze tak jest
    pier =pier.upper()
    drugie = drugie.upper()
    if len(pier)!=len(drugie):
        return False
    for i in pier:
        licz1=0
        licz2=0
        for j in pier:
            if j==i:
                licz1+=1
        for j in drugie:
            if j ==i:
                licz2+=1
        if licz2!=licz1:
            return False
    return True
#HORNER HORNER HORNER HORNER HORNER
def wieloHorner(wspolczynniki, x, stopien):
    if stopien==0:
        return wspolczynniki[0]
    return wieloHorner(wspolczynniki,x,stopien-1)*x + wspolczynniki[stopien]
  
#sprawne wyszukiwanie wartości w posortowanej tabeli, przydaje sie w dużych
def szukBin(tab, ele, p,k):
    if tab[p]==ele:
        return p
    if tab[k]==ele:
        return k
    if p==k:
        return -1
    mid=(p+k)//2
    if tab[mid]==ele:
        return mid
    elif tab[mid]>ele:
        return szukBin(tab,ele,p,mid)
    else:
        return szukBin(tab,ele,mid,k)
#HANOI, tego chyb nigdy nie skumam, 7 razy uczyłem się tego od nowa i tak chyba już zostanie, macie dwa rekur rozwiazania moje i to lepsze, oficjalne 
#na środku zawsze AC
# po bokach zawsze tyle ile ruchuw wczesniej
#z lewej zamienia się B-C a z prawej A-B

def hanoi(wys):
    if wys==1:
        return "AC"
    strona=hanoi(wys-1)
    lewa=""
    prawa=""

    for i in strona:
        if i=='B':
            lewa+='C'
            prawa+='A'
        if i == 'C':
            lewa+='B'
            prawa+=i
        if i =='A':
            lewa+=i
            prawa+='B'
    return lewa+"AC"+prawa

wynik=hanoi(5)

for index in range(0,len(wynik),2):
    print(wynik[index],"->",wynik[index+1])

#na środku zawsze AC
# po bokach zawsze tyle ile ruchuw wczesniej
#z lewej zamienia się B-C a z prawej A-B

def hanoi(wys,a,b,c):
    if wys==0:
        return ""
    L=hanoi(wys-1,a,c,b)
    P=hanoi(wys-1,b,a,c)
    return L+a+c+P

wynik=hanoi(5,'A','B','C')

for index in range(0,len(wynik),2):
    print(wynik[index],"->",wynik[index+1])
