quantMat = int(input("Quantas matérias você já fez? "))

materias = {}

def addMateria():
    nome = input("Insira o nome da matéria: ")
    peso = int(input("Insira o peso da matéria: "))
    nota = input(f"Insira sua nota em {nome}: ")
    materias[nome] = {"peso": peso, "nota": nota}

for _ in range(quantMat):
    addMateria()

for i in materias:
    nota = materias[i]["nota"]
    if nota == "a":
        materias[i]["nota"] = 4
    elif nota == "b":
        materias[i]["nota"] = 3
    elif nota == "c":
        materias[i]["nota"] = 2
    elif nota == "d":
        materias[i]["nota"] = 1
    elif nota == "o":
        materias[i]["nota"] = 0
    elif nota == "f":
        materias[i]["nota"] = 0
    
quo = 0
notaInd = 0

for i in materias:
    peso = materias[i]["peso"]
    nota = materias[i]["nota"]
    notaInd += nota*peso
    quo += peso

cr = notaInd/quo
print(cr)
