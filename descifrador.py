FILE_PATH = "cifrado.txt"
LETRAS_ORDENADAS_FRECUENCIA = [
    "E",
    "A",
    "O",
    "S",
    "R",
    "N",
    "I",
    "D",
    "L",
    "C",
    "T",
    "U",
    "M",
    "P",
    "B",
    "G",
    "V",
    "Y",
    "Q",
    "H",
    "F",
    "Z",
    "J",
    "Ñ",
    "X",
    "K",
    "W",
]


def cuenta_letras(texto) -> [()]:
    cuenta = {}
    for letra in texto:
        if letra in cuenta:
            cuenta[letra] += 1
        else:
            cuenta[letra] = 1
    return sorted(cuenta.items(), key=lambda x: x[1], reverse=True)


def letter_swapper(texto) -> str:
    letra_sustituible = ""
    while letra_sustituible.upper() not in LETRAS_ORDENADAS_FRECUENCIA:
        letra_sustituible = input("Introduce la letra que quieres sustituir: ")
    
    letra_sustituta = 0
    while letra_sustituta not in LETRAS_ORDENADAS_FRECUENCIA:
        letra_sustituta = input(f"Introduce la letra de sustitución para {letra_sustituible}: ")

    texto_resultado = ""
    for letra in texto:
        if letra == letra_sustituible:
            letra = letra_sustituta
        texto_resultado += letra
    
    return texto_resultado

def bucle_descifrado(texto, frecuencia) -> str:
    empezar = True
    while empezar:
        texto_auxiliar = texto
        continuar = True
        while continuar:
            print(texto_auxiliar)
            print(f"La frecuencia original de las letras es:\n{frecuencia}")
            texto_auxiliar = letter_swapper(texto_auxiliar)
            continuar = (input("\nDesea continuar? (Y/N) ").upper() == "Y")
        
        empezar = (input("\nDesea volver a empezar? (Y/N) ").upper() == "Y")
    return texto_auxiliar

def main():
    with open(FILE_PATH, "r") as archivo:
        texto_cifrado = archivo.read()

    cuenta = cuenta_letras(texto_cifrado)
    with open("estadistica.txt", "w") as estadistica:
        frecuencia = "\n".join([f"{tupla[0]}: {tupla[1]} (potencialmente {LETRAS_ORDENADAS_FRECUENCIA[indice]})" for indice, tupla in enumerate(cuenta)])
        estadistica.write(frecuencia)

    texto_resultado = bucle_descifrado(texto_cifrado, frecuencia)

    with open("resultado.txt", 'w') as resultado:
        resultado.write(texto_auxiliar)

if __name__ == "__main__":
    main()