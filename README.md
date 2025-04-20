# 📡 Plataforma SmartCampus - Monitoramento Inteligente Distribuído

Português (Brasil) | English (US)

---

## 🇧🇷 Português (Brasil)

Este projeto simula uma plataforma distribuída para **monitoramento em tempo real de ambientes inteligentes** (salas, laboratórios e auditórios). A arquitetura emprega sensores simulados, comunicação via gRPC e Sockets, middleware assíncrono e painel web para visualização dos dados.

### 🧠 Arquitetura

```
Sensor (UDP) 
   ↓
Gateway (UDP → gRPC)
   ↓
Microsserviço gRPC com fila (Queue)
   ↓
Arquivo de dados
   ↓
Painel web (Streamlit)
```

### 🎯 Objetivos

- Simular sensores em ambientes inteligentes
- Garantir comunicação confiável via sockets e gRPC
- Usar middleware (fila) para desacoplamento
- Exibir informações em tempo real no painel gerencial
- Publicar o painel na nuvem com Streamlit Cloud

### ⚙️ Tecnologias Utilizadas

- Python 3.11
- Sockets UDP
- gRPC
- `queue.Queue` como middleware
- Streamlit
- GitHub + Streamlit Cloud

### 📁 Organização do Projeto

| Pasta / Arquivo             | Função                                                  |
|-----------------------------|----------------------------------------------------------|
| `sensors/sensor_temperatura.py` | Simulador de temperatura (UDP)                          |
| `gateway/gateway_grpc.py`       | Recebe via UDP e envia via gRPC                         |
| `grpc_services/`               | Microsserviço com interface e servidor gRPC             |
| `middleware/fila.py`           | Fila de mensagens com `queue.Queue`                    |
| `painel/painel.py`             | Painel web com Streamlit                               |
| `dados_sensor.txt`             | Armazenamento simples dos dados simulados              |

### 🚀 Como Executar Localmente

```bash
python -m grpc_services.servidor_grpc
python gateway/gateway_grpc.py
python sensors/sensor_temperatura.py
streamlit run painel/painel.py
```

### ☁️ Painel Online

🔗 [https://plataforma-smartcampuss.streamlit.app](https://plataforma-smartcampuss.streamlit.app)

### 💻 Repositório

GitHub: [github.com/brumelido/plataforma-smartcampuss](https://github.com/brumelido/plataforma-smartcampuss)

### ✨ Feito com dedicação por Bruna Melido para a disciplina de Programação Distribuída e Paralela.

---

## 🇺🇸 English (US)

This project simulates a distributed platform for **real-time monitoring of smart environments** (classrooms, labs, auditoriums). It integrates simulated sensors, gRPC and socket communication, asynchronous middleware, and a web panel.

### 🧠 Architecture

```
Sensor (UDP) 
   ↓
Gateway (UDP → gRPC)
   ↓
gRPC Microservice with Queue
   ↓
Data file
   ↓
Web Panel (Streamlit)
```

### 🎯 Goals

- Simulate temperature sensors in real-time
- Ensure efficient and scalable communication
- Use middleware to decouple system components
- Provide real-time data visualization in a user-friendly panel
- Deploy the panel to the cloud via Streamlit Cloud

### ⚙️ Technologies Used

- Python 3.11
- UDP Sockets
- gRPC
- `queue.Queue` (as middleware)
- Streamlit
- GitHub + Streamlit Cloud

### 📁 Project Structure

- `sensors/sensor_temperatura.py`: Simulated temperature sensor
- `gateway/gateway_grpc.py`: Receives sensor data and forwards via gRPC
- `grpc_services/`: gRPC server and protocol definitions
- `middleware/fila.py`: Message queue
- `painel/painel.py`: Real-time monitoring panel

### 🚀 Run Locally

```bash
python -m grpc_services.servidor_grpc
python gateway/gateway_grpc.py
python sensors/sensor_temperatura.py
streamlit run painel/painel.py
```

### ☁️ Online Panel

🔗 [https://plataforma-smartcampuss.streamlit.app](https://plataforma-smartcampuss.streamlit.app)

### 💻 Source Code

GitHub: [github.com/brumelido/plataforma-smartcampuss](https://github.com/brumelido/plataforma-smartcampuss)

### ✨ Made with care by Bruna Melido for the Distributed and Parallel Programming course.