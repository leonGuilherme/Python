# pede a quantidade de produtos a serem cadastrados
n = int(input("Digite a quantidade de frutas ou verduras: "))
produtos = []
# pede informações destes produtos
for i in range(n):
    nome = input("Digite o nome do produto: ")
    if any(produto[0] == nome for produto in produtos):
        print("Produto já cadastrado")
    else:
        preco = float(input("Digite o preço do produto: "))
        produtos.append((nome, preco))
# busca o produto com suas informações
while True:
    busca = input(
        "Digite o nome do Fruta para buscar o preço (ou 'Fim' para encerrar): ")
    if busca == 'Fim':
        break
    produto_encontrado = next(
        (produto for produto in produtos if produto[0] == busca), None)
    if produto_encontrado:
        print(f"Preço: {produto_encontrado[1]}")
    else:
        print("Produto não cadastrado")
