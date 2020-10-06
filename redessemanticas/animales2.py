import json

Conocimiento = False
with open("data.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data["conocimientos"]
    print(data)


def esta(A, verbo,  B, Vi):
    if not Vi:
        return False
    c = 0
    f = len(Vi)
    while c < f:
        if Vi[c][0] == A and Vi[c][1] == verbo and Vi[c][2] == B:
            return True
        c = c + 1
    else:
        return False


def dat1(A):
    def dat2(B):
        def lista(Vi):
            def verbo(verb):
                return esta(A, verb, B, Vi)
            return verbo
        return lista
    return dat2

##################---Wrappers---##############3
def tiene_(val1, val2):
    return dat1(val1)(val2)(Conocimiento)("tiene")


def vive_(val1, val2):
    return dat1(val1)(val2)(Conocimiento)("vive")


def es_(val1, val2):
    return dat1(val1)(val2)(Conocimiento)("es")


def main():
    print("Bienvenido al programa")
    print('Puedes consultar escribiendo alguna de las siguientes opciones: \n'
          'tiene_("<Animal>", "<Caracteristica>") \n'
          'vive_("<Animal>", "<Elemento>") \n'
          'es_("<Animal>", "<Clasificación>")')
    print("Para salir presiona 'q' o escribe quit()")
    Terminar = False
    while not Terminar:
        Leer = input("> ")
        if(Leer == 'q'):
            return
        Imprimir = eval(Leer)
        print(Imprimir)


if __name__ == "__main__":
    main()
#tiene_("arraña", "pelo")
#tiene_("gato", "garras")
#vive_("gallo", "agua")
#vive_("tortuga", "agua")
#es_("mammalia", "mammalia")
#es_("oviparo", "tetrapodo")
