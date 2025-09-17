import csv
def lista_completa():
    arquivoopen = open("dadosjogos.csv")
    arquivoreader = csv.DictReader(arquivoopen)
    for linha in arquivoreader:
        print(linha)
def lista_linha_unica():
    arquivoopen = open("dadosjogos.csv")
    arquivoreader = csv.DictReader(arquivoopen)
    for linha in arquivoreader:
        if linha["Nome"] == "Fortnite":
            print(linha)

lista_completa()
