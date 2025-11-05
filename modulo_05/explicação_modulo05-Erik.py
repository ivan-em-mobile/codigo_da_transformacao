def calcula_media(notas):
    """Calcula a média de uma lista de notas."""
    # sum(notas) soma todos os itens da lista
    # len(notas) conta quantos itens há na lista
    return sum(notas) / len(notas) # 

def verificar_aprovacao(media):
    """Verifica se o aluno foi aprovado (média >= 7)."""
    if media >= 7:
        return "O aluno(a) está aprovado(a)🥳" # 
    else:
        return "O aluno(a) está reprovado(a)😢" # 


print("Cálculo de Média e Verificação de Aprovação")
print("\n-------------------------------------------")


# Notas do aluno
notas_aluno = input("Insira as notas do aluno separadas por um espaço: ")
notas_aluno = [float(nota) for nota in notas_aluno.split(' ')]

# Chamando as funções
media_final = calcula_media(notas_aluno)
status_aluno = verificar_aprovacao(media_final)

# Exibindo o resultado
print(f"Notas: {notas_aluno}")
print(f"Média: {media_final:.2f}")
print(f"Status: {status_aluno}")