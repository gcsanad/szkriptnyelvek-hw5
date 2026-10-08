
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    visszakuldendo = ""
    for c in text:
        if c in chars:
            visszakuldendo += c
    return visszakuldendo


def main():
    print(valid("Barking!"))                              
    print(valid("KL754", "0123456789"))                   
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))

if __name__ == "__main__":
    main()