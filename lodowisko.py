import math


def oblicz_niewiadoma(wynik1, wynik2, przyblizenie=0.00001, poczatkowa_var=0.000001):
    """
    Oblicz równanie w postaci x = wiadoma * niewiadoma

    :param wynik1: Znana wartość
    :param wynik2: Wartość z niewiadomą
    :return: Szacowana wartość niewiadomej z
    """

    u = poczatkowa_var
    while not math.isclose(wynik1, wynik2 * u, rel_tol=przyblizenie):
        try:
            u += 0.000001
            if u > wynik1 / 100:
                u = None
                print("Obliczenia nierealne. Sprawdź przybliżenie.")
                break
        except KeyboardInterrupt:
            u = None
            print("Przerwano obliczenia")
            break

    return u
