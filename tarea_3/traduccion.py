

def traducir(palabra):
    with open("EN-ES.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split("=")
            if len(partes) == 2:
                palabra_dicc, palabra_destino = partes
                if palabra_dicc == palabra and palabra_destino != "":
                    return palabra_destino
    return None
print("==========================")
print("TRADUCTOR ESPAÑOL A INGLES ") 
print("==========================")

palabra = input("Ingresa la palabra a traducir: ")
traduccion = traducir(palabra)
if traduccion is not None:
 print(f"Traducción: {traduccion}")
else:
 ("palabra incorrecta")   