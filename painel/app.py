from flask import Flask, render_template
import os

app = Flask(__name__)

CAMINHO_ARQUIVO = os.path.abspath("../dados_sensor.txt")

@app.route('/')
def index():
    dado = "-"
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as f:
            linhas = f.readlines()
            if linhas:
                dado = linhas[-1].strip()

    print(f"[PAINEL] Último dado lido: {dado}")  # 💡 Adiciona isso pra debug

    if ":" in dado:
        tipo, valor = map(str.strip, dado.split(":"))
    else:
        tipo, valor = "-", "-"

    return render_template('index.html', tipo=tipo, valor=valor)

if __name__ == '__main__':
    app.run(debug=True)