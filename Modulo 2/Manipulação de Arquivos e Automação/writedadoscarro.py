import csv
with open("carro.csv", "a", newline="") as adicionar:
    escrever= csv.writer(adicionar)
    escrever.writerow(["Carro foda", "legal", "2025", "200.000.000"])
