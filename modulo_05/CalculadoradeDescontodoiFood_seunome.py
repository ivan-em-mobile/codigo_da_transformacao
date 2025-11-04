'''
simulador de cálculo de desconto para pedidos no iFood.
Se o valor do pedido for maior ou igual a R$ 50,00, aplica um desconto de 10%.
'''
def calcular_valor_final(valor_pedido, taxa_entrega, desconto=0.10):
    """
    Calcula o valor total do pedido, aplicando desconto se for >= R$ 50.00.
    """
    valor_com_desconto = valor_pedido
    
    print(f"\nDetalhes do Cálculo:")
    print(f"  > Valor do Pedido: R${valor_pedido:.2f}")
    
    # Condição de Desconto
    if valor_pedido >= 50.00:
        valor_descontado = valor_pedido * desconto
        valor_com_desconto = valor_pedido - valor_descontado
        print(f"  > Desconto de {desconto*100:.0f}% aplicado! (-R${valor_descontado:.2f})")
    else:
        print("  > Sem desconto (valor abaixo de R$50,00).")
    
    # Cálculo Final
    valor_total = valor_com_desconto + taxa_entrega
    
    return valor_total

# --- Interação do Usuário ---

print("--- Simulador de Pedido iFood ---")

# 1. Solicita a entrada de dados do usuário e converte para float
try:
    valor_pedido_usuario = float(input("Digite o valor total dos itens do pedido (ex: 45.90): "))
    taxa_entrega_usuario = float(input("Digite o valor da taxa de entrega (ex: 7.50): "))
except ValueError:
    print("\nERRO: Certifique-se de que inseriu valores numéricos válidos.")
    # Define valores de fallback para evitar quebra do código
    valor_pedido_usuario = 0.0
    taxa_entrega_usuario = 0.0

# 2. Chama a função com os dados do usuário
if valor_pedido_usuario > 0:
    valor_final = calcular_valor_final(
        valor_pedido=valor_pedido_usuario, 
        taxa_entrega=taxa_entrega_usuario
    )
    
    print(f"\nTaxa de Entrega: R${taxa_entrega_usuario:.2f}")
    print(f"O VALOR TOTAL FINAL a ser pago é: **R${valor_final:.2f}**")