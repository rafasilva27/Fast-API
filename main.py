from fastapi import FastAPI

app = FastAPI() #criando a instância do FastAPI

vendas = {
    1: {"item": "camiseta", "preco_unitario": 50, "quantidade": 10},
    2: {"item": "tenis", "preco_unitario": 100, "quantidade": 5},
    3: {"item": "chinelo", "preco_unitario": 20, "quantidade": 20},
}

@app.get("/")
def home():
    return {"Bem vindo a minha API"}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda] #retorna a venda correspondente ao id
    else:
        return {"Erro": "ID inexistente"}

@app.get("/vendas")
def listar_vendas():
    return vendas #retorna a lista de vendas

@app.get("/quantidades")
def quantidade():
    return {"quantidade total": len(vendas)} #retorna a quantidade de vendas

@app.post("/vendas")
def adicionar_venda():
    vendas.update({4: {"item": "camiseta", "preco_unitario": 50, "quantidade": 10}}) #adiciona um novo item
    return vendas

@app.put("/vendas/{id_venda}/precos/{preco}")
def atualizar_venda(id_venda: int, preco: float):
    vendas[id_venda] = {"item": "calça", "preco_unitario": preco, "quantidade": 1}
    return vendas