import csv
def marca_ford():
    arquivoopen = open("carro.csv")
    arquivoreader = csv.DictReader(arquivoopen)
    for linha in arquivoreader:
        if linha["Marca"] == "Ford":
            print(linha)
def ano_carro():    
    arquivoopen = open("carro.csv")
    arquivoreader = csv.DictReader(arquivoopen)
    for linha in arquivoreader:
        if linha["Ano"] == "2022":
            print(linha)
def str_para_int():
    arquivoopen = open("carro.csv")
    arquivoreader = csv.DictReader(arquivoopen) 
    for linha in arquivoreader:
        if int(linha["Valor"] < "50000"):
            print(linha)

marca_ford()
