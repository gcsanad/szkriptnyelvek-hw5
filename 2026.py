import datetime

# datetime importálása a main függvényben történik, hogy a kód futtatásakor a jelenlegi év kiírásra kerüljön. 

def main():
    print(datetime.datetime.now().year)
if __name__ == "__main__":
    main()