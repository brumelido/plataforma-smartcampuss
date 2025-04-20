import socket
import grpc
import sys
import os

# Importa os arquivos gerados do gRPC
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grpc_services import sensor_pb2, sensor_pb2_grpc

# Conexão com o servidor gRPC
canal = grpc.insecure_channel('localhost:5050')
cliente = sensor_pb2_grpc.SensorServiceStub(canal)

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("[Gateway gRPC] Aguardando dados dos sensores...")

while True:
    data, addr = sock.recvfrom(1024)
    mensagem = data.decode()
    print(f"[Gateway] Recebeu: {mensagem}")

    tipo, valor = mensagem.split(":")
    dado = sensor_pb2.DadoSensor(tipo=tipo, valor=valor)
    resposta = cliente.EnviarDado(dado)
    print(f"[Gateway → gRPC] Resposta: {resposta.mensagem}")
