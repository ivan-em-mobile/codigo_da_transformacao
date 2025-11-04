# Exemplo de Código Base para o Módulo 4
# Criando uma lista para armazenar as tarefas
tarefas = ["Estudar Python", "Fazer exercícios", "Comprar café"]

def adicionar_tarefa(descricao):
    tarefas.append(descricao)
    print(f"Tarefa '{descricao}' adicionada.")

def listar_tarefas():
    print("\n--- LISTA DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            # Acessando por índice (0-based)
            print(f"{i+1}. {tarefa}")

# --- Execução ---
adicionar_tarefa("Revisar Módulo 4")
listar_tarefas()

# Remover a primeira tarefa
tarefas.pop(0) 
print("\nApós remover a primeira tarefa:")
listar_tarefas()