print("OIS je zakon!")


def izpis(visina: float) -> None:
    """
    Izpis gravitacijskega pospeška na <visina> kilometrih.

    @param: visina (float): nadmorska višina v kilometrih
    """
    print(f"Gravitacijski pospešek na {visina} km nadmorske visine je {izracunGravitacije(visina * 1000):.2f} m/s^2.")