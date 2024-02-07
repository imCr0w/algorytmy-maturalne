#sorki za chaos, ale tu jest wszystko co zapisałem z nauki rok temu, zalecam zapisać to sobie w obsdianie, to ładnie się pokoloruje
## czy liczba jest pierwsza
```cpp
bool czy_pierwsza(int a)
{
    int m = sqrt(a);
    int i = 2;
    while(i<=m)
    {
        if(a%i==0)
        {
            return 0;
        }
        i++;    
    }
    return 1;
}
```


## dec2hex(int b)
```cpp
string dec2hex(int b)
{
    stringstream ss;
    ss << hex << b;
    string res ( ss.str() );
    return res;
}
```

## hex2dec(string c)
```cpp
int hex2dec(string c)
{
    int wynik;
    stringstream ss;
    ss << c;
    ss >> hex >> wynik;
    return wynik;
}
```

## any2dec(string number, int base)
```cpp
int toDecimal(string number,int base)
{
    int decimal= 0;
    int size = number.length();
    for(int i=0; i<size; i++) //check for each position
    {
        //calculate digit * base^position for each position

        if(number[i]>='A') // if it has more than 10 digits
        {
            decimal += (number[i]-'A'+10) *pow(base,size-i-1);
        }
        else
        {
            decimal += (number[i]-'0') *pow(base,size-i-1);
        }
    }
    return decimal;
}
```

## dec2any(int dec, int baza)
```cpp
string dec2any(int a, int baza)
{
    string odp="";
    int odp2=0;
    int b,c;
    char d;
    c=0;
    if(baza<10)
    {
        b=a;
        while(b>baza)
        {
            odp2+=(b%baza)*pow(10,c);
            c++;
            b=b/baza;
        }
        odp2+=b*pow(10,c);
        odp=to_string(odp2);
        return odp;
    }
    else
    {
        while(a>baza)
        {
            b=a%baza;
            if(b>9)
            {
                d=b+65-10;
            }
            else
            {
                d=b+48;
            }
            a=a/baza;
            odp=d+odp;
        }
        if(a>9)
        {
            d=a+65-10;
        }
        else
        {
            d=a+48;
        }
        odp=d+odp;
        return odp;
    }
}
```

## odwrócenie liczby
```cpp
int reverse(int a)
{
    int b,c;
    string as;
    b=0;
    as = to_string(a);
    c = as.size();
    for(int i=0;i<c;i++)
    {
        b+= (a%10)*pow(10,c-i-1);
        a=a/10;
    }
    return b;
}
```

## Wielokroności
```cpp
bool czy_ma_wk(int a,int tab[200])
{
    for(int i=0;i<200;i++)
    {
        if(tab[i]%a==0&&a<tab[i])
        {
            return true;
        }
    }
    return false;
}

int gdzie_wielk(int a, int tab[200])
{
    for(int i=0;i<200;i++)
    {
        if(tab[i]%a==0&&a<tab[i])
        {
            return i;
        }
    }
}

int naj_wk(int a,int tab[200])
{
    int odp=100000;
    for(int i=0;i<200;i++)
    {
        if(tab[i]%a==0&&a<tab[i]&&odp>tab[i])
        {
            odp=tab[i];
        }
    }
    return odp;
}

int nast_wk(int a, int b, int tab[200])
{
    int odp=100000;
    for(int i=0;i<200;i++)
    {
        if(tab[i]%a==0&&a<tab[i]&&odp>tab[i]&&tab[i]>b)
        {
            odp=tab[i];
        }
    }
    return odp;
}

int ile_naj(int a, int tab[200],int b)
{
    int odp;
    if(czy_ma_wk(a,tab)==0)
    {
        return 1;
    }
    else
    {
        if(czy_ma_wk(b,tab)==1)
        {
            return 1+ile_naj(b,tab,naj_wk(b,tab));
        }
        else
        {
            return 1+ile_naj(nast_wk(a,b,tab),tab,a);
        }
    }
}
```

## NWW i NWD
```cpp
int nwd (int a, int b)
{
    int c;
    while(b!=0)
    {
        c=a%b;
        a=b;
        b=c;
    }
    return a;
}

int nww(int a, int b)
{
    return a*b/nwd(a,b);
}
```

## sortowanie bubble
```cpp
void bubble(int *tab, int ile)
{
    for(int i=i;i<ile;i++)
    {
        for(int j = ile-1;j>=1;j--)
        {
            if(tab[j]<tab[j-1])
            {
                int bufor;
                bufor=tab[j-1];
                tab[j-1]=tab[j];
                tab[j]=bufor;
            }

        }
    }
}
```

## Hanoi
```cpp
void hanoi(int n, char a, char b, char c)
{
    if(n==0)
    {
        return;
    }
    hanoi(n-1,a,c,b);
    cout<<"przenies dysk "<<n<<" z slupka "<< a << " na slupek "<< b<<endl;
    hanoi(n-1,c,b,a);
}
```

## Fibonacci
```cpp
int ciagFiba(int a)
{
    if(a==1||a==2)
    {
        return 1;
    }
    else
    {
        return ciagFiba(a-1)+ciagFiba(a-2);
    }
}
```

## silnia
```cpp
int silnia(int a)
{
    if(a==1)
    {
        return 1;
    }
    else
    {
        return a*silnia(a-1);
    }
}
```

## potega 
```cpp
int potega(int a, int wykl)
{
    if(wykl==1)
    {
        return a;
    }
    else
    {
        return a*potega(a,wykl-1);
    }
}
```

## horner
```cpp
int appHor(int wpspol[], int stop, int x)
{
    if(stop==0)
    {
        return wpspol[0];
    }
    else
    {
        return x*appHor(wpspol,stop-1,x)+wpspol[stop];
    }
}
```

## rekur na sys <10
```cpp
int naSys(int a, int baza)
{
    if(a<baza)
    {
        return a;
    }
    return naSys(a/baza,baza)*10+a%baza;

}
```

## odwrocenie rekur
```cpp
string odwrocenie(string a, int rozm)
{
    string odp="";
    if(rozm==1)
    {
        odp+=a[0];
        return odp;
    }
    char b = a[rozm-1];
    return b+odwrocenie(a,rozm-1);
}
```


## Wyszukiwanie binarne rekur w posortowanej tabeli
```cpp
string wyszBin(int a, int *tab, int po, int ko)
{
    int sr = (po+ko)/2;
    if(sr==ko||sr==po)
    {
        return "nie ma";
    }
    if(a==tab[sr])
    {
        string odp = to_string(sr);
        return odp;
    }
    if(a<tab[sr])
    {
        return wyszBin(a, tab, po, sr);
    }
    else
    {
        return wyszBin(a,tab,sr,ko);
    }

}
```

## sito Erystotenesa
```cpp
	
	
	int N=1000;
    int sito[N];
    int j;

    sito[1]=0;

    for(int i=2;i<N;i++)
    {
        sito[i]=1;
    }

    for(int i=2;i<N;i++)
    {
        if(sito[i]==1)
        {
            j=i*i;
            while(j<=N)
            {
                sito[j]=0;
                j=j+i;
            }
        }
    }
```



## pierwiastek blisko
```cpp
float pier(int x, float d)
{
    float a=1;
    while(fabs(a-(x/a))>d)
    {
        a=(a+(x/a))/2;
    }
    return a;
}
````


## ile czynników pierwszych
```cpp
int ile_czyn_p(int a)
{
    int k=2;
    int ile=0;
    while(a>1)
    {
        while(a%k==0)
        {
            a=a/k;
            ile++;
        }
        k++;
    }
    return ile;
}

````


## dec2any<10
```cpp
int dex2any(int a, int base)
{
    int odp=0;
    int b=a;
    int c=0;
    while(b>=base)
    {
        odp+=(b%base)*pow(10,c);
        c++;
        b=b/base;
    }
    odp+=b*pow(10,c);
    return odp;
}
```
## Sortowoanie quicksort
```cpp
void quicksort(int *tablica, int lewy, int prawy)
{
//v to oś, i to p a j to q
    int v=tablica[(lewy+prawy)/2];
    int i,j,x;
    i=lewy;
    j=prawy;
    do
    {
        while(tablica[i]<v) i++;
        while(tablica[j]>v) j--;
        if(i<=j)
        {
            x=tablica[i];
            tablica[i]=tablica[j];
            tablica[j]=x;
            i++;
            j--;
        }
    }
    while(i<=j);
    if(j>lewy) quicksort(tablica,lewy, j);
    if(i<prawy) quicksort(tablica, i, prawy);
}
```


## NWD Euklidesa rec
```cpp
int gcd(int a, int b)
{
    if(b==0)
    {
        return a;
    }
    return gcd(b,a%b);
}
```
