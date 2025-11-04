# Lista principal para o catálogo (com uma série inicial para visualização)
catalogo_series = [{
    "titulo": "The Crown",
    "genero": "Drama Histórico",
    "episodios_assistidos": 25,
    "total_episodios": 60,
    "nota_usuario": 9.2
}]

print("--- Adicionar Nova Série ao Catálogo ---")

# 1. Solicita a entrada de dados do usuário
novo_titulo = input("Digite o título da nova série: ")
novo_genero = input("Digite o gênero da nova série: ")

# É importante converter a entrada de strings para números (int)
try:
    novos_assistidos = int(input("Quantos episódios você já assistiu? "))
    novo_total = int(input("Qual é o total de episódios da série? "))
    nova_nota = float(input("Qual nota você daria para a série (0 a 10)? "))
except ValueError:
    print("Erro: Por favor, insira números válidos para episódios e nota.")
    novos_assistidos, novo_total, nova_nota = 0, 1, 0.0

# 2. Cria o novo Dicionário com as informações inseridas
nova_serie = {
    "titulo": novo_titulo,
    "genero": novo_genero,
    "episodios_assistidos": novos_assistidos,
    "total_episodios": novo_total,
    "nota_usuario": nova_nota
}

# 3. Adiciona a nova série à lista
catalogo_series.append(nova_serie)

print("\n--- Catálogo Atualizado ---")
# 4. Imprime todas as séries e o progresso
for serie in catalogo_series:
    # Evita divisão por zero
    if serie["total_episodios"] > 0:
        percentual = (serie["episodios_assistidos"] / serie["total_episodios"]) * 100
    else:
        percentual = 0
        
    print(f"\nSérie: **{serie['titulo']}** ({serie['genero']})")
    print(f"Progresso: {percentual:.2f}% | Nota: {serie['nota_usuario']}")