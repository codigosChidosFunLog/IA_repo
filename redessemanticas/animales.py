Tie = [
    ("tortuga", "garras"),
    ("tortuga", "Proteccion queratina"),
    ("gallo", "garras"),
    ("gallo", "Proteccion queratina"),
    ("cocodrilo", "garras"),
    ("cocodrilo", "Proteccion queratina"),
    ("iguana", "garras"),
    ("iguana", "Proteccion queratina"),
    ("gato", "g. mamarias"),
    ("gato", "pelo"),
    ("gato", "garras"),
    ("ballena", "g. mamarias"),
    ("ballena", "pelo"),
    ("oso", "g. mamarias"),
    ("oso", "pelo"),
    ("oso", "garras"),
    ("delfin", "g. mamarias")
]
Viv = [
    ("tortuga", "agua"),
    ("gallo", "tierra"),
    ("cocodrilo", "agua"),
    ("iguana", "tierra"),
    ("gato", "tierra"),
    ("ballena", "agua"),
    ("oso", "tierra"),
    ("delfin", "agua")
]

Ser = [
    ("tortuga", "sauropsida"),
    ("gallo", "sauropsida"),
    ("cocodrilo", "sauropsida"),
    ("iguana", "sauropsida"),
    ("gato", "mammalia"),
    ("ballena", "mammalia"),
    ("oso", "mammalia"),
    ("delfin", "mammalia"),
    ("mammalia", "viviparo"),
    ("viviparo", "tetrapodo"),
    ("sauropsida", "oviparo"),
    ("oviparo", "tetrapodo"),
    ("tetrapodo", "vertebrado")
]


def esta(A,B,Vi):
    if not Vi:
        return False
    c = 0
    f = len(Vi)
    while c < f:
        if Vi[c][0] == A and Vi[c][1] == B:
            return True
        c = c + 1
    else:
        return False


def dat1(A):
    def dat2(B):
        def lista(Vi):
            return esta(A,B,Vi)
        return lista
    return dat2

##################---Wrappers---##############3
def Tiene(val1, val2):
    return dat1(val1)(val2)(Tie)


def Vive(val1, val2):
    return dat1(val1)(val2)(Viv)


def Es(val1, val2):
    return dat1(val1)(val2)(Ser)


print(Tiene("arraña", "pelo"))
print(Tiene("gato", "garras"))
print(Vive("gallo", "agua"))
print(Vive("tortuga", "agua"))
print(Es("mammalia", "mammalia"))
print(Es("oviparo", "tetrapodo"))
