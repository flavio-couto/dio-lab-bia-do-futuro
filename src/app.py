import json
import pandas as pd
import requests
import streamlit as st

# ============= CONFIGURAÇÃO =============

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============= CARREGAR DADOS =============

perfil = json.load(open('C:/Users/Pichau/Desktop/Dio/perfil_investidor.json'))
produtos = json.load(open('C:/Users/Pichau/Desktop/Dio/produtos_financeiros.json'))
transacoes = pd.read_csv('C:/Users/Pichau/Desktop/Dio/historico_atendimento.csv')
historico = pd.read_csv('C:/Users/Pichau/Desktop/Dio/transacoes.csv')


# ============= MONTAR CONTEXTO =============

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: {perfil['patrimonio_total']} | RESERVA: {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============= SYSTEM PROMPT =============

SYSTEM_PROMPT = f"""

Você é o FinancIA, um agente financeiro inteligente especializado em educação financeira.
Você irá se comportar como um agente de IA (FinancIA) e seu objetivo é ensinar conceitos sobre finanças pessoais de uma forma simples e amigável, você pode usar os dados do cliente para dar exemplos práticos.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Use linguagem simples e seja didático
5. Pergunte se o cliente entendeu
"""

# ============= CHAMAR OLLAMA =============

def perguntar():
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============= INTERFACE =============

st.title("FinancIA, seu educador financeiro mais legal")

if pergunta := st.chat_input("Digite aqui a sua dúvida sobre finanças: "):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant".write(perguntar(pergunta)))
