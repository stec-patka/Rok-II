# moja grupa

def func_map(func, lista):
    return [func(x) for x in lista]

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

print(sumuj_napisy( ("Jan", "Kowalski"), ("Anna", "Nowak") ))


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
        if self.current >= len(self.napis):
            raise StopIteration

        znak = self.napis[self.current]

        # 2. Warunek specyficzny zadania: "kończy przy znaku niebędącym cyfrą"
        if znak not in self.mapa:
            raise StopIteration

        wynik = self.mapa[znak]
        self.current += 1
        return wynik


numbers = {
    '0': 'zero ',
    '1': 'jeden ',
    '2': 'dwa ',
    '3': 'trzy ',
    '4': 'cztery ',
    '5': 'pięć ',
    '7': 'siedem ',
    '8': 'osiem ',
    '9': 'dziewięć '
}

word = str(input("enter a number: "))
result = ''
for char in word:
    if char in numbers:
        result += numbers[char]

print(result)


# trzecia grupa

def kwadraty(*args):
    for x in args:
        yield x**2

def znajdz_najmniejszy_indeks(lst):
    if not lst:
        return -1
    min_idx = 0
    min_wartosc = lst[0]
    for idx, wartosc in enumerate(lst):
        if wartosc < min_wartosc:
            min_wartosc =wartosc
            min_idx = idx
    return min_idx

def wszystkie(fun, lst):
    for x in lst:
        if not fun(x):
            return False
    return True


def rzymski_na_arabski(napis):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0

    # Zabezpieczenie na wypadek pustego napisu
    if not napis:
        return 0

    while i < len(napis) - 1:
        val1 = roman_values[napis[i]]
        val2 = roman_values[napis[i + 1]]

        if val1 >= val2:
            total += val1
        else:
            total -= val1
        i += 1

    total += roman_values[napis[-1]]
    return total


class Wektor:
    def __init__(self, lista):
        self.lista = lista

    def __str__(self):
        return str(self.lista)

    def __add__(self, other):
        wynik = []

        dl_self = len(self.lista)
        dl_other = len(other.lista)

        if dl_self > dl_other:
            limit = dl_self
        else:
            limit = dl_other

        # Pętla wykonuje się tyle razy, ile ma dłuższy wektor
        for i in range(limit):

            # Pobieranie z pierwszego wektora (self)
            if i < dl_self:
                wynik.append(self.lista[i])
            else:
                wynik.append(0)  # Dopełnienie zerem, gdy zabraknie liczb

            # Pobieranie z drugiego wektora (other)
            if i < dl_other:
                wynik.append(other.lista[i])
            else:
                wynik.append(0)  # Dopełnienie zerem

        return Wektor(wynik)


# grupa czwarta

def generator_slow(liczba):
    slownik_cyfr = {
        '0': 'zero',
        '1': 'jeden',
        '2': 'dwa',
        '3': 'trzy',
        '4': 'cztery',
        '5': 'pięć',
        '6': 'sześć',
        '7': 'siedem',
        '8': 'osiem',
        '9': 'dziewięć'
    }
    napis = str(liczba)

    for znak in napis:
        yield slownik_cyfr[znak]


from abc import ABC, abstractmethod
class Figura(ABC):
    licznik = 0
    def __init__(self):
        #super().__init__()
        Figura.licznik +=1

    @abstractmethod
    def obwod(self):
        pass

class Prostokat(Figura):
    licznik = 0
    def __init__(self, bok_a, bok_b):
        super().__init__()
        Prostokat.licznik +=1
        self.bok_a = bok_a
        self.bok_b = bok_b

    def obwod(self):
        return 2 * (self.bok_a + self.bok_b)

def sumuj_krotki2(krotki):
    return [k[0] + k[1] for k in krotki]

def znajdz_litere(text, litera):
    wynik = []
    for idx, char in enumerate(text):
        if char == litera:
            wynik.append(idx)
    return wynik


def sprawdz(func, lst):
    for x in lst:
        if func(x):
            return True
    return False