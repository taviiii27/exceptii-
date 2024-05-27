#5
def returneaza_valoare(cheie):
    dictionar = {"a": 1, "b": 2, "c": 3}
    try:
        valoare = dictionar[cheie]
        return valoare
    except KeyError:
        return "Cheia nu există în dicționar"

print(returneaza_valoare("a"))  
print(returneaza_valoare("d"))  
