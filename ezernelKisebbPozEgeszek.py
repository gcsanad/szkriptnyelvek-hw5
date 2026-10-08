def main():
    # Állapítsuk meg azon 1000-nél kisebb számok összegét, melyek 3-nak vagy 5-nek a többszörösei. 
    szamokOsszege = sum([n for n in range(1000) if n % 3 == 0 or n % 5 == 0])
    print("Összeg:", szamokOsszege)

if __name__ == "__main__":
    main()