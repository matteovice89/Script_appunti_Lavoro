def format_mac(s):
    return ':'.join(s[i:i+2] for i in range(0, len(s), 2))

# input: stringhe separate da spazio
input_str = input("Inserisci le stringhe separate da spazio: ")

# divido in lista
lista = input_str.split()

# trasformo tutte
risultati = [format_mac(s) for s in lista]

# output
print("Risultato:")
for r in risultati:
    print(r)
