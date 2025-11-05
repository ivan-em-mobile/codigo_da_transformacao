def calcula_media(notas):
    """Calcula a média de uma lista de notas."""
    # sum(notas) soma todos os itens da lista
    # len(notas) conta quantos itens há na lista
    return sum(notas) / len(notas) # 

def verificar_aprovacao(media):
    """Verifica se o aluno foi aprovado (média >= 7).
    
    """
    if media >= 7:
        return "Aprovado" # 
    else:
        return "Reprovado" # 


def ler_notas():
    """Lê as notas do usuário e retorna uma lista de floats."""
    while True:
        entrada = input("Insira as notas do aluno separadas por vírgula (ex: 7.5, 8, 9): ").strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        # normaliza separadores comuns para vírgula e remove entradas vazias
        for sep in [';', ' ']:
            entrada = entrada.replace(sep, ',')
        partes = [p.strip() for p in entrada.split(',') if p.strip() != '']
        try:
            notas = [float(p) for p in partes]
            if len(notas) == 0:
                print("Nenhuma nota válida encontrada. Tente novamente.")
                continue
            return notas
        except ValueError:
            print("Formato inválido. Use números separados por vírgula (ex: 8,7.5,10). Tente novamente.")

# Chamando as funções
notas_aluno = ler_notas()
media_final = calcula_media(notas_aluno)
status_aluno = verificar_aprovacao(media_final)

# Exibindo o resultado
print(f"Notas: {notas_aluno}")
print(f"Média: {media_final:.2f}")
print(f"Status: {status_aluno}")