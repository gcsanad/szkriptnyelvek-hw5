# Állapítsuk meg azon számjegyek összegét, amelyek azonosak a rákövetkező számjeggyel. A számsorozat cirkuláris, vagyis az utolsó számjegy rákövetkezője a legelső számjegy. Próbáljuk meg használni a zip() függvényt. List comprehension-t be tudunk csempészni? 

def inverse_captcha(szamjegyek):
    """Visszaadja azon számjegyek összegét, amelyek azonosak a rákövetkező számjeggyel.
    
    A számsorozat cirkuláris, vagyis az utolsó számjegy rákövetkezője a legelső számjegy.
    """
    szamjegyek = [int(szam) for szam in str(szamjegyek)]
    return sum(szam for szam, kov_szam in zip(szamjegyek, szamjegyek[1:] + szamjegyek[:1]) if szam == kov_szam)

def main():
    # A bemenet egy számsorozat.
    bemenet = input("Kérem a számsorozatot: ")
    print("Az eredmény:", inverse_captcha(bemenet))

if __name__ == "__main__":
    main()