import socket
import sys
import os  # <- ESSA LINHA FALTAVA!

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from middleware.fila import fila_mensagens

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("[Gateway] Aguardando dados dos sensores...")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    print(f"[Gateway] Recebeu: {message}")

    # Adiciona mensagem à fila
    fila_mensagens.put(message)