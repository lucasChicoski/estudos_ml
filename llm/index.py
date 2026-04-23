import ollama
import json
import os

prompt = """
Você é um assistente de codigo responde no seguinte formato: 

Formato:
{
    "bot": "Ola, tudo bem?",
    "code: "printf('')",
}

não gere nada além do objeto {}
Responda SOMENTE com JSON válido.
Use apenas aspas duplas.
Não inclua texto antes ou depois.
Se não souber, retorne:
{"acao": "nenhuma"}
"""

client = ollama.Client(
    host="http://host.docker.internal:11434",
)


response = client.chat(
    model="llama3.1",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "Imoplemente para mim a sequencia de fibonacci em javascript"}
    ]
)

def criar_arquivo(nome, conteudo):
    with open(nome, "w") as f:
        f.write(conteudo)
    return True


criar_arquivo(f'llm/teste.js', 'asdasd')