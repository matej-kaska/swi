class Calculator:
    def __init__(self):
        self.pamet = 0

    def secti(a,b):
        if isinstance(a, str) or isinstance(b, str):
            try:
                a = float(a)
                b = float(b)
            except Exception as e:
                print("ChybaVstupu")
        return a + b

    def odecti(a,b):
        if isinstance(a, str) or isinstance(b, str):
            try:
                a = float(a)
                b = float(b)
            except Exception as e:
                print("ChybaVstupu")
        return a - b

    def vynasob(a,b):
        if isinstance(a, str) or isinstance(b, str):
            try:
                a = float(a)
                b = float(b)
            except Exception as e:
                print("ChybaVstupu")
        return a * b

    def deleni(a,b):
        if isinstance(a, str) or isinstance(b, str):
            try:
                a = float(a)
                b = float(b)
            except Exception as e:
                print("ChybaVstupu")
        if b == 0:
            print("ChybaVstupu")
            return "Nelze dělit nulou"
        return a / b

def main():
    kalkulacka = Calculator()

    while True:
        print("Vyberte operaci: +, -, *, /")
        operace = input()
        print("Zadejte první číslo:")
        a = input()
        print("Zadejte druhé číslo: (může být prázdné, bude použita pamět kalkulačky)")
        b = input()
        if b == "":
            b = kalkulacka.pamet
        if operace == "+":
            vysledek = kalkulacka.secti(a,b)
        elif operace == "-":
            vysledek = kalkulacka.odecti(a,b)
        elif operace == "*":
            vysledek = kalkulacka.vynasob(a,b)
        elif operace == "/":
            vysledek = kalkulacka.deleni(a,b)
        kalkulacka.pamet = vysledek
        print("Výsledek je " + str(vysledek))
        input()

def test_runner():
    test_secti_cela_cisla()
    test_secti_desetinna_cisla()
    test_secti_stringy()
    test_odecti_cela_cisla()
    test_odecti_desetinna_cisla()
    test_odecti_stringy()
    test_vynasob_cela_cisla()
    test_vynasob_desetinna_cisla()
    test_vynasob_stringy()
    test_deleni_cela_cisla()
    test_deleni_desetinna_cisla()
    test_deleni_stringy()
    test_deleni_nulou()

# testy na sčítání

def test_secti_cela_cisla():
    kalkulacka = Calculator()
    a, b = 2, 3
    vysledek = kalkulacka.secti(a,b)
    assert vysledek == 5

def test_secti_cela_cisla():
    kalkulacka = Calculator()
    a, b = 2, 3
    vysledek = kalkulacka.secti(a,b)
    assert vysledek == 5

def test_secti_desetinna_cisla():
    kalkulacka = Calculator()
    a, b = 2.5, 1.3
    vysledek = kalkulacka.secti(a,b)
    assert vysledek == 3.8

def test_secti_stringy():
    kalkulacka = Calculator()
    a, b = "2.5", "1.3"
    vysledek = kalkulacka.secti(a,b)
    assert vysledek == 3.8

# testy na odčítání

def test_odecti_cela_cisla():
    kalkulacka = Calculator()
    a, b = 2, 3
    vysledek = kalkulacka.odecti(a,b)
    assert vysledek == -1

def test_odecti_desetinna_cisla():
    kalkulacka = Calculator()
    a, b = 2.5, 1.3
    vysledek = kalkulacka.odecti(a,b)
    assert vysledek == 1.2

def test_odecti_stringy():
    kalkulacka = Calculator()
    a, b = "2.5", "1.3"
    vysledek = kalkulacka.odecti(a,b)
    assert vysledek == 1.2

# testy na nasobení

def test_vynasob_cela_cisla():
    kalkulacka = Calculator()
    a, b = 2, 3
    vysledek = kalkulacka.vynasob(a,b)
    assert vysledek == 6

def test_vynasob_desetinna_cisla():
    kalkulacka = Calculator()
    a, b = 2.5, 1.3
    vysledek = kalkulacka.vynasob(a,b)
    assert vysledek == 3.25

def test_vynasob_stringy():
    kalkulacka = Calculator()
    a, b = "2.5", "1.3"
    vysledek = kalkulacka.vynasob(a,b)
    assert vysledek == 3.25

# testy na dělení

def test_deleni_cela_cisla():
    kalkulacka = Calculator()
    a, b = 6, 3
    vysledek = kalkulacka.deleni(a,b)
    assert vysledek == 2

def test_deleni_desetinna_cisla():
    kalkulacka = Calculator()
    a, b = 2.25, 1.5
    vysledek = kalkulacka.deleni(a,b)
    assert vysledek == 1.5

def test_deleni_stringy():
    kalkulacka = Calculator()
    a, b = "2.25", "1.5"
    vysledek = kalkulacka.deleni(a,b)
    assert vysledek == 1.5

def test_deleni_nulou():
    kalkulacka = Calculator()
    a, b = 5, 0
    vysledek = kalkulacka.deleni(a,b)
    assert vysledek == "Nelze dělit nulou"

if __name__ == "__main__":
    test_runner()
    main()
