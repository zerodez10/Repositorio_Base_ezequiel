# pergunta_2= "s"
# while pergunta_2 == "s":
#     pergunta = int(input(f"Qual número inteiro desejado? "))
#     if pergunta %2 == 0:
#         print(f"O número é par")
#     else:
#         print(f"O número é impar")
#     pergunta_2 = input(f"Deseja repetir? (s/n): ")
numero = int(input("Qual número inteiro desejado? "))
if numero <= 0:
    print(f"Número inválido.")
else:
    for i in range(1, numero + 1):
        print(i)
