# app.py
import json
import os
from flask import Flask, request, jsonify

# Configuração: Nome do arquivo JSON onde os votos serão salvos.
VOTOS_FILE = 'votos.json'
app = Flask(__name__)

# --- Funções de Manipulação do JSON (Persistência) ---

def load_votos():
    """Carrega os votos do arquivo JSON ou retorna um dicionário vazio."""
    if os.path.exists(VOTOS_FILE):
        try:
            with open(VOTOS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Caso o arquivo esteja vazio ou corrompido, retorna vazio.
            return {}
    return {}

def save_votos(votos):
    """Salva o dicionário de votos atualizado no arquivo JSON."""
    with open(VOTOS_FILE, 'w', encoding='utf-8') as f:
        # 'indent=4' é para formatar o JSON de forma legível.
        json.dump(votos, f, indent=4)

# --- Endpoint 1: Votar (Método POST) ---

@app.route('/votar', methods=['POST'])
def votar_filme():
    """
    Registra um novo voto. Requer um JSON no corpo da requisição com a chave 'filme'.
    """
    
    # 1. Obter dados do corpo da requisição
    dados = request.get_json() 
    
    # 2. Validação
    if not dados or 'filme' not in dados:
        return jsonify({"erro": "Campo 'filme' é obrigatório."}), 400

    # 3. Processamento
    filme = dados['filme'].title() # Normaliza para capitalização correta
    votos = load_votos()
    
    # Adiciona 1 voto ao filme. Se for a primeira vez, inicia com 1.
    votos[filme] = votos.get(filme, 0) + 1
    
    save_votos(votos)

    # 4. Retorno (201 Created)
    return jsonify({"mensagem": f"Voto registrado para {filme}!", "votos_atuais": votos[filme]}), 201


# --- Endpoint 2: Ranking (Método GET) ---

@app.route('/ranking', methods=['GET'])
def mostrar_ranking():
    """
    Retorna o ranking dos filmes ordenado pela quantidade de votos.
    """
    
    votos = load_votos()
    
    # 1. Ordenação: Ordena por contagem de votos (item[1]), do maior para o menor.
    ranking = sorted(votos.items(), key=lambda item: item[1], reverse=True)
    
    # 2. Formatação para JSON
    ranking_formatado = [{"filme": f, "votos": v} for f, v in ranking]
    
    # 3. Retorno (200 OK)
    return jsonify({"ranking": ranking_formatado})


# --- Execução do Aplicativo ---
if __name__ == '__main__':
    app.run(debug=True)