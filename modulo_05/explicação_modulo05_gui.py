'''
Exemplo de Código Base para o Módulo 5
'''

# def cal_media():
def calcula_media(notas):
    """Calcula a média de uma lista de notas."""
    # sum(notas) soma todos os itens da lista
    # len(notas) conta quantos itens há na lista
    return sum(notas) / len(notas) #

def verificar_aprovacao(media):
    """Verifica se o aluno foi aprovado (média >= 7).
    Como poderiamos colocar as quantidades de faltas aqui?"""
    if media >= 7:
        return "Aprovado" #
    else:
        return "Reprovado" #

def ler_notas_input(prompt="Insira as notas do aluno separadas por vírgula (ex: 8.0, 7.5, 6): "):
    """Lê e valida notas do usuário, retornando uma lista de floats."""
    while True:
        entrada = input(prompt).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        partes = [p.strip() for p in entrada.split(',') if p.strip()]
        try:
            notas = [float(p) for p in partes]
            if len(notas) == 0:
                print("Nenhuma nota válida encontrada. Tente novamente.")
                continue
            return notas
        except ValueError:
            print("Formato inválido. Use números separados por vírgula, ex: 8.0,7.5,6")
            continue

# Notas do aluno (lidas do input)
notas_aluno = ler_notas_input()

# Chamando as funções
media_final = calcula_media(notas_aluno)
status_aluno = verificar_aprovacao(media_final)

# Exibindo o resultado
print(f"Notas: {notas_aluno}")
print(f"Média: {media_final:.2f}")
print(f"Status: {status_aluno}")