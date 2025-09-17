import json
def atividade1():
    dados_json = '{"produto":"Caderno", "preco": 12.5, "estoque": 30}'
    dados_python = json.loads(dados_json)
    print(f"Produto é: {dados_python["produto"]}")
    print(f"Preço é: {dados_python["preco"]}")
def atividade2():
    aluno = {
        "nome": "Lucas",
        "idade": 16,
        "aprovado": True
    }
    aluno_2 = json.dumps(aluno)
    print(aluno_2)
def atividade3():
    dados = {
        "filme": "Matrix",
        "ano": 1999,
        "genero": "Ficcao Cientifica"
    }
    m = json.dumps(dados, indent = 4)
    print(m)
atividade1()
