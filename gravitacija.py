print("OIS je zakon!")

def izracun_gravitacije(visina: float) -> float:
    """
    Za podano nadmorsko višino izračuna gravitacijski pospešek.
    """
    C = 6.674e-11
    M = 5.5972e24
    r = 6.371e6
    return (C * M) / (r + visina ** 2)
