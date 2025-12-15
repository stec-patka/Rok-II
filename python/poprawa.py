# moja grupa

def func_map(func, lista):
    return [func[x] for x in lista]

class Kwadraty:
    def __init__(self, start, end=None):
        if end is None:
            self.start = 1
            self.end=start
        else:
            self.start=start
            self.end=end

        self.current = self.start

    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        wynik = self.current**2
        self.current +=1
        return wynik

def sumuj_napisy(*args):
    return [" ".join(para) for para in args]
    #return [f"{imie} {nazwisko}" for imie, nazwisko in pary]


def podaj_numery(slownik, szukane_nazwisko):
    numery = []
    for (imie, nazwisko), numer in slownik.items():
        if nazwisko == szukane_nazwisko:
            numery.append(numer)
    return numery
    #return [numer for (imie, nazwisko), numer in slownik.items() if nazwisko == szukane_nazwisko]

def podaj_indeksy(lst, num):
    szukany_idx = -1
    for indeks, elem in enumerate(lst):
        if elem == num :
            szukany_idx = indeks
    return szukany_idx


#  pierwsza grupa

def func_filter(filtr, lista):
    return [x for x in lista if filtr(x)]

def na_napis(*args, sep = "++"):
    return sep.join(str(x) for x in args)

def znajdz_wartosc(lst, num):
    for indeks, elem in enumerate(lst):
        if elem == num:
            return indeks
    return -1

def sumuj_krotki(krotki):
    return [k1 + k2 for k1, k2 in krotki]

class Slownie:
    mapa = {
        '0': 'zero',
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'piec',
        '6': 'szesc',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewiec',
    }
    def __init__(self,napis):
        self.napis = napis
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 1. Warunek końca danych (koniec napisu)
        if self.current >= len(self.napis):
            raise StopIteration

        znak = self.napis[self.current]

        # 2. Warunek specyficzny zadania: "kończy przy znaku niebędącym cyfrą"
        if znak not in self.mapa:
            raise StopIteration

        # 3. Zwracanie wyniku i inkrementacja
        wynik = self.mapa[znak]
        self.current += 1
        return wynik


# trzecia grupa

def kwadraty(*args):
    for x in args:
        yield x**2

def znajdz_najmniejszy_indeks(lst):
    if not lst:
        return -1
    min_idx = 0
    najmniejsza_wartosc = lst[0]
    for idx, wartosc in enumerate(lst):
        if wartosc < najmniejsza_wartosc:
            najmniejsza_wartosc =wartosc
            min_idx = idx
    return min_idx

def wszystkie(fun, lst):
    for x in lst:
        if not fun(x):
            return False
    return True