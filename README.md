# Plataforma SmartCampus – Monitoramento de Ambientes Inteligentes

Este projeto simula uma plataforma distribuída para monitoramento e controle de ambientes inteligentes, utilizando sensores simulados, gateway com sockets, comunicação via gRPC e painel web.

## 🔧 Tecnologias utilizadas

- Python
- gRPC
- Socket UDP
- Fila (`queue.Queue`)
- Streamlit
- (Opcional: deploy na nuvem)

## 🧩 Estrutura do sistema

- `sensor_temperatura.py`: simula um sensor de temperatura que envia dados via socket UDP.
- `gateway/GatewayGRPC.py`: recebe os dados do sensor e envia para o microsserviço via gRPC.
- `grpc_services/`: microsserviço gRPC que recebe os dados e grava em `dados_sensor.txt`.
- `painel.py`: painel gerencial feito em Streamlit.
- `dados_sensor.txt`: arquivo onde os dados são gravados para leitura pelo painel.

## ▶️ Como executar localmente

1. Execute `grpc_services/servidor_grpc.py`
2. Em outro terminal, execute `gateway/GatewayGRPC.py`
3. Em outro terminal, execute `sensor_temperatura.py`
4. Em outro terminal, execute `painel.py` com:
