from concurrent import futures
import grpc
import sys
import os

# Garante que o Python ache sensor_pb2 e sensor_pb2_grpc
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import sensor_pb2
import sensor_pb2_grpc

class SensorService(sensor_pb2_grpc.SensorServiceServicer):
    def EnviarDado(self, request, context):
        print(f"[gRPC] Recebido: {request.tipo} = {request.valor}")

        # ✅ Aqui dentro, grava no arquivo
        with open("dados_sensor.txt", "a") as f:
            f.write(f"{request.tipo}:{request.valor}\n")

        return sensor_pb2.Resposta(mensagem="Dado recebido com sucesso!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensor_pb2_grpc.add_SensorServiceServicer_to_server(SensorService(), server)
    server.add_insecure_port('[::]:5050')
    server.start()
    print("[gRPC] Servidor rodando na porta 5050")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()