# Münchhausen számok ellenőrzése
from itertools import combinations_with_replacement
from collections import Counter


def digit_power(digit):
    """Ellenőrzi a 0^0 esetetét, amelyet a definíció szerint 0-nak vesz fel."""
    return 0 if digit == 0 else digit ** digit


def check_if_munchausen(n):
    """Visszaadja, hogy n Münchhausen-szám-e."""
    if n < 0:
        return False

    digits = str(n)
    return sum(digit_power(int(digit)) for digit in digits) == n


def find_munchausen(limit):
    """Megkereshetőtıti a Münchhausen számokat a limit határig.

    A szamjegyeket egyetlen érvényes multiset-ként kapja meg, így nem
    kell minden egész számot külön ellenőrizni.
    """
    if limit < 0:
        return []

    found = []
    max_digits = len(str(limit))

    for digit_count in range(1, max_digits + 1):
        for digits in combinations_with_replacement(range(10), digit_count):
            candidate = sum(digit_power(digit) for digit in digits)
            candidate_digits = Counter(str(candidate))
            input_digits = Counter(str(digit) for digit in digits)
            if candidate < limit and candidate_digits == input_digits:
                found.append(candidate)

    return sorted(set(found))


def main():
    limit = 10_000
    munchausen_numbers = find_munchausen(limit)
    print("A 10 000-nél kisebb Münchhausen számok:", munchausen_numbers)

    # 440 000 000 határig is használható, de a keresés a számok
    # számjegy-összetettése szerint fog működni, nem egyes számok szerint.
    all_numbers = find_munchausen(440_000_000)
    print("A 440 000 000 határig található Münchhausen számok:", all_numbers)


if __name__ == "__main__":
    main()