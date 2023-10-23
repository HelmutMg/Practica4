price_bitcoin = [5200.60,6400.80,6900.70,5100.60,5800.90,7100.50,6200.30]

name_arch = "price_bitcoin.txt"

# Abrir el archivo en modo escritura
with open(name_arch, "w") as archivo:
    
    for price in price_bitcoin:
        archivo.write(f"{price:.2f}\n")

print(f"Los precios de Bitcoin se han guardado en '{name_arch}'")