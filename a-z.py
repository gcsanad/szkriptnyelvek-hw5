"""
Írjanak egy a-z.py nevű szkriptet, amit lefuttatva megkapjuk az angol ábécé kisbetűit a-tól z-ig. 
Tegyünk egy szimbolikus linket a szkriptre z-a.py néven. 
A z-a.py -t futtatva viszont az angol ábécé kisbetűit fordítva szeretnénk megkapni, vagyis z-től a-ig. 
"""
import sys

def main():
    if sys.argv[0].endswith("z-a.py"):
        print("".join(chr(i) for i in range(ord('z'), ord('a') - 1, -1)))
    else:
        print("".join(chr(i) for i in range(ord('a'), ord('z') + 1)))

if __name__ == "__main__":
    main()