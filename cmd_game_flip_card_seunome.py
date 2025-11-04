import random
import time

# --- MÓDULO 4: ESTRUTURAS DE DADOS (Listas e Dicionários) ---

# Define os pares do jogo
SIMBOLOS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
CARTAS_DO_JOGO = SIMBOLOS * 2 # Cria 16 cartas (8 pares)

# Estado inicial do tabuleiro (Todas as cartas 'escondidas' com *)
TAMANHO_TABULEIRO = 4
TABULEIRO_ESCONDIDO = [['*' for _ in range(TAMANHO_TABULEIRO)] for _ in range(TAMANHO_TABULEIRO)]

# --- MÓDULO 5: FUNÇÕES EM PYTHON ---

def inicializar_e_embaralhar(cartas):
    """
    Embaralha as cartas e as organiza em uma matriz 4x4.
    Retorna: a matriz do jogo (o "gabarito").
    """
    random.shuffle(cartas)
    
    tabuleiro_gabarito = []
    
    # Organiza a lista embaralhada em 4 linhas de 4 colunas
    for i in range(0, len(cartas), TAMANHO_TABULEIRO):
        tabuleiro_gabarito.append(cartas[i:i + TAMANHO_TABULEIRO])
        
    return tabuleiro_gabarito

def exibir_tabuleiro(tabuleiro_exibicao):
    """
    Função para imprimir o tabuleiro no console, com coordenadas para o usuário.
    """
    print("\n  ", end="")
    # Exibe os números das colunas (0, 1, 2, 3)
    for col in range(TAMANHO_TABULEIRO):
        print(f" {col}", end=" ")
    print("\n  " + "---" * TAMANHO_TABULEIRO)
    
    # Exibe as cartas e os números das linhas (0, 1, 2, 3)
    for linha in range(TAMANHO_TABULEIRO):
        print(f"{linha}|", end=" ")
        for simbolo in tabuleiro_exibicao[linha]:
            print(f"{simbolo} ", end=" ")
        print() # Quebra de linha no final da linha

def verificar_jogada(gabarito, escondido, jogada1, jogada2):
    """
    Recebe as coordenadas das duas jogadas e verifica se formam um par.
    """
    (l1, c1) = jogada1
    (l2, c2) = jogada2
    
    # Pega os símbolos no tabuleiro (Gabarito)
    simbolo1 = gabarito[l1][c1]
    simbolo2 = gabarito[l2][c2]
    
    # 1. Verifica se são um par
    if simbolo1 == simbolo2:
        print(f"\n✨ PAR ENCONTRADO! O símbolo é: {simbolo1}")
        # Mantém as cartas visíveis no tabuleiro 'escondido'
        escondido[l1][c1] = simbolo1 
        escondido[l2][c2] = simbolo2
        return True
    else:
        print("\n❌ Não é um par. As cartas serão viradas novamente.")
        # O tempo de espera simula a carta 'virando'
        time.sleep(2) 
        # Como não é um par, o tabuleiro 'escondido' não muda.
        return False

# --- LÓGICA PRINCIPAL DO JOGO ---

def iniciar_jogo():
    """Função principal que gerencia o fluxo do jogo."""
    
    # M4: Inicializa o gabarito (matriz com os símbolos embaralhados)
    tabuleiro_gabarito = inicializar_e_embaralhar(CARTAS_DO_JOGO)
    # M4: Inicializa o que será exibido para o usuário (só asteriscos)
    tabuleiro_escondido = [['*' for _ in range(TAMANHO_TABULEIRO)] for _ in range(TAMANHO_TABULEIRO)]
    
    pares_encontrados = 0
    max_pares = len(SIMBOLOS)
    
    print("--- JOGO DA MEMÓRIA (CONSOLE) ---")
    
    # M5: Loop principal do jogo
    while pares_encontrados < max_pares:
        exibir_tabuleiro(tabuleiro_escondido)
        print(f"\nPares Encontrados: {pares_encontrados} de {max_pares}")

        # Função interna para pegar uma jogada válida do usuário
        def pegar_jogada(numero):
            while True:
                try:
                    coord = input(f"JOGADA {numero}: Digite Linha e Coluna (ex: 0,3): ")
                    l, c = map(int, coord.split(','))
                    # M4: Validação de índices
                    if 0 <= l < TAMANHO_TABULEIRO and 0 <= c < TAMANHO_TABULEIRO and tabuleiro_escondido[l][c] == '*':
                        return (l, c)
                    else:
                        print("Coordenadas inválidas ou carta já encontrada/virada. Tente novamente.")
                except:
                    print("Formato inválido. Use Linha,Coluna (ex: 1,2).")

        # M5: Chamada de função para a primeira carta
        jogada_1 = pegar_jogada(1)
        l1, c1 = jogada_1
        
        # M4: Mostra temporariamente a primeira carta no console
        tabuleiro_escondido[l1][c1] = tabuleiro_gabarito[l1][c1]
        exibir_tabuleiro(tabuleiro_escondido)
        
        # M5: Chamada de função para a segunda carta
        jogada_2 = pegar_jogada(2)
        l2, c2 = jogada_2
        
        # M4: Mostra temporariamente a segunda carta
        tabuleiro_escondido[l2][c2] = tabuleiro_gabarito[l2][c2]
        exibir_tabuleiro(tabuleiro_escondido)
        
        # M5: Chamada de função para verificar o resultado
        if verificar_jogada(tabuleiro_gabarito, tabuleiro_escondido, jogada_1, jogada_2):
            pares_encontrados += 1
        else:
            # Se não for par, vira as cartas de volta
            tabuleiro_escondido[l1][c1] = '*' 
            tabuleiro_escondido[l2][c2] = '*'
            exibir_tabuleiro(tabuleiro_escondido) # Mostra o tabuleiro atualizado

    # Fim do jogo
    print("\n🏆 PARABÉNS! Você encontrou todos os pares!")

# Inicia o jogo
iniciar_jogo()