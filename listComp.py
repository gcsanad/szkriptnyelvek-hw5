def main():
    #1. Feladat
    kozlEszk = ['auto', 'villamos', 'metro']
    kozlMegoldas = [n.upper() + '!' for n in kozlEszk]

    print("1.feladat:", kozlMegoldas)

    #2. Feladat
    nevek = ['aladar', 'bela', 'cecil']
    nevekMegoldas = [n.capitalize() for n in nevek]

    print("2.feladat:", nevekMegoldas)

    #3. Feladat
    nullasLista = [0 for n in range(10)]

    print("3.feladat:", nullasLista)

    #4. Feladat
    szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    szamokMegoldas = [n*2 for n in szamok]

    print("4.feladat:", szamokMegoldas)

    #5. Feladat
    stringSzamok = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    stringSzamokMegoldas = [int(n) for n in stringSzamok]

    print("5.feladat:", stringSzamokMegoldas)

    #6. Feladat
    szamString = "1234567"
    szamStringLista = [int(n) for n in szamString]

    print("6.feladat:", szamStringLista)

    #7. Feladat
    szoveg = 'The quick brown fox jumps over the lazy dog'
    szovegSzamok = [len(n) for n in szoveg.split()]

    print("7.feladat:", szovegSzamok)

    #8. Feladat
    pySzoveg = "python is an awesome language" 
    pySzovegMegoldas = [n[0] for n in pySzoveg.split()]

    print("8.feladat:", pySzovegMegoldas)

    #9. Feladat
    pySzamokSzoveg = 'The quick brown fox jumps over the lazy dog'
    pySzamokSzovegMegoldas = [(pySzamokSzoveg.split()[n], len(pySzamokSzoveg.split()[n])) for n in range(len(pySzamokSzoveg.split()))]

    print("9.feladat:", pySzamokSzovegMegoldas)

    #10. Feladat
    tiznelKisebb = [n for n in range(10) if n % 2 == 0]

    print("10.feladat:", tiznelKisebb)

    #11. Feladat
    husznalKisebbParosNegyzet = [n**2 for n in range(20) if n**2 % 2 == 0]

    print("11.feladat:",    husznalKisebbParosNegyzet)

    #12. Feladat
    neggyelVegzodoNegyzetek = [n**2 for n in range(20) if n**2 % 10 == 4]

    print("12.feladat:", neggyelVegzodoNegyzetek)

    #13. Feladat
    abcNagybetui = [chr(n) for n in range(65, 91)]
    osszefuzottNagybetuk = ''.join(abcNagybetui)

    print("13.feladat:", osszefuzottNagybetuk)

    #14. Feladat
    whitespacesSzavek = [' apple ', ' banana ', ' kiwi']
    whitespacesSzavakMegoldas = [n.strip() for n in whitespacesSzavek]

    print("14.feladat:", whitespacesSzavakMegoldas)

    #15. Feladat
    szamok = [1, 0, 1, 1, 0, 1, 0, 0]
    szamokMegoldas = ''.join([str(n) for n in szamok])

    print("15.feladat:", szamokMegoldas)

if __name__ == "__main__":
    main()