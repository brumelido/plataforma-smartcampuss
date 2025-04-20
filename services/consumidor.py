import time
import sys
import os

# Adiciona a pasta raiz ao path para importar 'middleware'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from middleware.fila import fila_mensagens

print("[Consumidor] Iniciado. Esperando mensagens...")

while True:
    if not fila_mensagens.empty():
        msg = fila_mensagens.get()
        print(f"[Consumidor] Processou mensagem: {msg}")
    time.sleep(1)
