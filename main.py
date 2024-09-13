"""
permet d'importer la fonction racine
"""
from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Vérifie qu'un nombre est premier

    Args:
        p (int) : nombre qu'on test
    Returns:
        bool : si p premier True, sinon False
    """
    if p==1:
        return False
    if 1<p<=3:
        return True
    for i in range (2,int(sqrt(p))+1):
        if p%i==0:
            return False
    return True

#### Fonction principale


def main():
    """
    appel à la fonction secondaire
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
