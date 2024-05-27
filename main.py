#6
def citeste_si_afiseaza_lungimea():
    try:
        text = input("Introduceți un text: ")
        if not isinstance(text, str):
            raise ValueError("Valoarea introdusă nu este un string.")
        print(f"Lungimea textului introdus este: {len(text)}")
    except ValueError as e:
        print(e)

citeste_si_afiseaza_lungimea()
