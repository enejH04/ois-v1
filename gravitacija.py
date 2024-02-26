print("OIS je zakon!")

def izracun_gravitacije(visina: float) -> float:
    """
    Za podano nadmorsko višino izračuna gravitacijski pospešek.
    """
    C = 6.674e-11
    M = 5.5972e24
    r = 6.371e6
    return (C * M) / (r + visina ** 2)

def izpis(visina: float) -> None:
    """
    Izpis gravitacijskega pospeška na <visina> kilometrih.

    @param: visina (float): nadmorska višina v kilometrih
    """
    print(f"Gravitacijski pospešek na {visina} km nadmorske visine je {izracun_gravitacije(visina * 1000):.2f} m/s^2.")
