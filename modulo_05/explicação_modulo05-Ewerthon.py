# Função para calcular a média das notas
def calcula_media(notas):
    return sum(notas) / len(notas)

# Função para verificar se o aluno foi aprovado
def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Função para ler e validar as notas
def ler_notas():
    while True:
        notas_input = input("Insira as notas do aluno separadas por vírgula: ")

        try:
            # Remove espaços e converte para float
            notas = [float(nota.strip()) for nota in notas_input.split(',') if nota.strip() != '']

            if len(notas) == 0:
                print("⚠️ Você não digitou nenhuma nota. Tente novamente.\n")
                continue

            # Verifica se as notas estão entre 0 e 10
            for nota in notas:
                if nota < 0 or nota > 10:
                    raise ValueError("As notas devem estar entre 0 e 10.")
            
            return notas

        except ValueError:
            print("❌ Entrada inválida! Digite apenas números separados por vírgulas, ex: 8, 7.5, 6\n")

# --- Programa principal ---
print("📘 Sistema de Avaliação de Alunos")
print("-" * 40)

while True:
    nome = input("\nDigite o nome do aluno: ").strip().title()
    notas_aluno = ler_notas()

    media_final = calcula_media(notas_aluno)
    status_aluno = verificar_aprovacao(media_final)

    print("\n📊 Resultado final:")
    print(f"Aluno: {nome}")
    print(f"Notas: {notas_aluno}")
    print(f"Média: {media_final:.2f}")
    print(f"Status: {status_aluno}")

    continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        print("\n✅ Programa finalizado. Até a próxima!")
        break
