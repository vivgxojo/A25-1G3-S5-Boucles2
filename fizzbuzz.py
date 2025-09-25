# fichier: fizzbuzz.py

def fizzbuzz(n: int) -> str:
    """
    Retourne "Fizz" si divisible par 3,
            "Buzz" si divisible par 5,
            "FizzBuzz" si divisible par 15,
            sinon la chaîne du nombre.
    Gère zéro et négatifs de la même façon.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


if __name__ == "__main__":
    try:
        n = int(input("Entrez un entier pour FizzBuzz : ").strip())
        print(fizzbuzz(n))
    except ValueError:
        print("Entrée invalide : entrez un entier.")
