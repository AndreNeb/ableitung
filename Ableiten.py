formel = input("Gib ein was Abgeleitet werden soll: ")
variableza = input("Nach welcher Variable soll abgeleitet werden: ")
menge = int(input("Wie oft soll abgeleitet werden: "))

formelhoch = ""
eableitung = True
indexvariable = formel.find(variableza)
length = len(formel)
indexhoch = formel.find("^")
indexgeschwungklammera = formel.find("(")
indexgeschwungklammere = formel.find(")")
indexln = formel.find("ln")
indexcos = formel.find("cos")
indexsin = formel.find("sin")
indextan = formel.find("tan")
indexmal = formel.find("*")
indexplus = formel.find("+")
indexwurzel = formel.find("wurzel")
indexe = formel.find("e")


def ableiten():
    global formel
    global variableza
    global menge
    global formelhoch
    global eableitung
    global indexvariable
    global length
    global indexhoch
    global indexgeschwungklammera
    global indexgeschwungklammere
    global indexln
    global indexcos
    global indexsin
    global indextan
    global indexmal
    global indexplus
    global indexwurzel
    global indexe

    if indexhoch != -1:
        formel = hoch(menge)

    if indexln != -1:
        formel = ln(menge)

    if indexcos != -1:
        formel = cos(menge)

    if indexsin != -1:
        formel = sin(menge)

    if indextan != -1:
        formel = tan(menge)

    if indexwurzel != -1:
        formel = wurzel(menge)

    if indexe != -1:
        formel = e(menge)
    return formel


def ln(menge):
    while menge != 0:
        menge = menge - 1
    return formel


def cos(menge):
    while menge != 0:
        menge = menge - 1
    return formel


def sin(menge):
    while menge != 0:
        menge = menge - 1
    return formel


def tan(menge):
    while menge != 0:
        menge = menge - 1
    return formel


def e(menge):
    while menge != 0:
        menge = menge - 1
    return formel


def wurzel(menge):
    while menge != 0:
        menge = menge - 1
    return formel


def hoch(menge):
    global formel
    global formelhoch
    global eableitung

    if indexmal != -1 and indexplus != -1:
        if indexmal < indexplus:
            formelhoch = formel[indexhoch + 1:indexmal]
        else:
            formelhoch = formel[indexhoch + 1:indexplus]
    else:
        formelhoch = formel[indexhoch + 1:length]

    if formelhoch.isdigit():
        formelhoch = int(formelhoch)
    koeff = 1  # später mal was vor x steht
    koeff1 = ""
    wert = 0
    formelhochn = formelhoch
    while menge != 0:
        if indexhoch != -1:
            if formel[indexhoch + 1] == 1 and eableitung == True:
                print(variableza)
            if type(formelhoch) == int:
                koeff = koeff * formelhoch
                wert = wert - 1
                formelhoch = formelhoch + wert
                formel = str(koeff) + "*" + str(variableza) + "^" + str(formelhoch)
                formelhoch = int(formelhoch) - 1
            else:
                if koeff1 != "":
                    koeff1 = koeff1 + ")*(" + formelhoch + str(wert)
                else:
                    koeff1 = koeff1 + str(formelhochn)
                wert = wert - 1
                formelhochn = formelhoch + str(wert)
                formel = "(" + koeff1 + ")" + "*" + str(variableza) + "^" + str(formelhochn)
            menge = menge - 1
            eableitung = False
    return formel


def variablensuchen(formel):
    indexvar = []
    for i in range(len(formel)):
        if formel[i].isalpha():
            indexvar.append(i)
    return indexvar


def innereableitung():
    global formelhoch
    variablensuchen(formelhoch)


print(ableiten())
