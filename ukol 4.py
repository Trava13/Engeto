def je_anagram(*args) -> bool:
    """
    Vrati boolean True, pokud jsou vsechny parametry anagramy.
    Jinak vrati False.

    Priklad:
    >>> print(je_anagram("ship", "hips", "hisp"))
    True
    >>> print(je_anagram_matous("ship", "hips", "duck"))
    False
    """
    vzor = sorted(args[0])
    print(vzor)

    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True


print(
    je_anagram("ship", "hips", "hisp"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)
