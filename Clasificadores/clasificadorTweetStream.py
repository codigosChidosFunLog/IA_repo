import json

Conocimiento = []
PalabrasTweet = {}
with open("probabilidadesClasificador.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data["Probabilidades"]
    print(Conocimiento)


def abrirArchivo(archivo):
    PalabrasTweet.clear()
    f = None
    try:
        f = open(archivo, "r")
        for line in f:
            for word in line.split():
                if word in PalabrasTweet:
                    PalabrasTweet[word] += 1
                else:
                    PalabrasTweet[word] = 1
    except IOError:
        print("Error al abrir el archivo")
    finally:
        if f is not None:
            f.close()
            #print(PalabrasTweet)


def buscarPalabras(palabra):
    c = 0
    f = len(Conocimiento)
    while c < f:
        if Conocimiento[c][0].lower() == palabra.lower():
            return Conocimiento[c][1]
        c += 1


def imprimirResultados(pila):
    con = 0
    acuProbabilidad = 0
    if not pila:
        print("No Stream")
    else:
        for x in pila:
            con += x[1]
            acuProbabilidad += (float(x[2]) * x[1])
        print("Probabilidad :", acuProbabilidad/con)
        print("Stream" if acuProbabilidad/con > 0.55 else "No Stream")


def analizar_(archivo):
    PilaProbabilidades = []
    abrirArchivo(archivo)
    for x in PalabrasTweet:
        probabilidad = buscarPalabras(x)
        if probabilidad:
            PilaProbabilidades.append((x, PalabrasTweet[x], probabilidad))
    #print(PilaProbabilidades)
    imprimirResultados(PilaProbabilidades)


def main():
    print('-----Biendenido al Clasificador de tweets-----')
    print('Puede consultar su archivo txt escribiendo la siguiente opcion')
    print('analizar_("<nombre_archivo>.txt") ejemplo: analizar_("tweet.txt")')
    print("Para salir presiona 'q' o escoribe quit()")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        eval(Leer)


if __name__ == "__main__":
    main()
