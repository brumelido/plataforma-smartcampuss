# CloudFormation Template - SmartCampus (com rota pública)

AWSTemplateFormatVersion: '2010-09-09'
Description: >
  Infraestrutura AWS para a Plataforma SmartCampus com Subnet pública, Internet Gateway e painel acessível.
Expandir
smartcampus-stack.yaml
3 KB
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 10:13
# 📡 Plataforma SmartCampus - Monitoramento Inteligente Distribuído

Português (Brasil) | English (US)

---
Expandir
README.md
5 KB
﻿
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
- Publicar o painel na nuvem com Streamlit Cloud ou AWS EC2

### ⚙️ Tecnologias Utilizadas

- Python 3.11
- Sockets UDP
- gRPC
- `queue.Queue` como middleware
- Streamlit
- GitHub + Streamlit Cloud ou AWS CloudFormation

### ☁️ Infraestrutura em Nuvem

Utilizamos AWS CloudFormation para automatizar o provisionamento da infraestrutura, incluindo:

- VPC, Subnet pública e Internet Gateway
- Security Group com liberação das portas 22 (SSH) e 8501 (Streamlit)
- Instância EC2 com Ubuntu Server 22.04 LTS
- Execução automática do painel Streamlit com `user_data`

Após o deploy, o painel ficou acessível via IP público pela porta 8501.

### 📁 Organização do Projeto

| Pasta / Arquivo             | Função                                                  |
|-----------------------------|----------------------------------------------------------|
| `sensors/sensor_temperatura.py` | Simulador de temperatura (UDP)                          |
| `gateway/gateway_grpc.py`       | Recebe via UDP e envia via gRPC                         |
| `grpc_services/`               | Microsserviço com interface e servidor gRPC             |
| `middleware/fila.py`           | Fila de mensagens com `queue.Queue`                    |
| `painel/painel.py`             | Painel web com Streamlit                               |
| `infra/smartcampus-stack.yaml` | Infraestrutura como código com CloudFormation          |
| `dados_sensor.txt`             | Armazenamento simples dos dados simulados              |

### 🚀 Como Executar Localmente

```bash
python -m grpc_services.servidor_grpc
python gateway/gateway_grpc.py
python sensors/sensor_temperatura.py
streamlit run painel/painel.py
```

### ☁️ Como Executar na Nuvem

1. Acesse o serviço AWS CloudFormation
2. Faça upload do arquivo `smartcampus-stack.yaml`
3. Crie a pilha e aguarde
4. Copie o IP público da instância criada
5. Acesse em: `http://<IP_PUBLICO>:8501`

### 💻 Repositório

GitHub: [github.com/brumelido/plataforma-smartcampuss](https://github.com/brumelido/plataforma-smartcampuss)

### ✨ Feito com dedicação por Bruna Melido e Isadora Lacerda para as disciplinas de Programação Distribuída e Computação em Nuvem.

---

## 🇺🇸 English (US)

This project simulates a distributed platform for **real-time monitoring of smart environments** such as classrooms, labs, and auditoriums. The system architecture includes simulated sensors, gRPC and socket-based communication, asynchronous middleware, and a real-time web panel using Streamlit.

### 🧠 Architecture

```
Sensor (UDP)
   ↓
Gateway (UDP → gRPC)
   ↓
gRPC microservice with Queue
   ↓
Data file
   ↓
Web panel (Streamlit)
```

### ☁️ Cloud Infrastructure

We used **AWS CloudFormation** to automatically provision the necessary infrastructure:

- VPC with public Subnet and Internet Gateway
- Security Group allowing ports 22 (SSH) and 8501 (Streamlit)
- EC2 Instance with Ubuntu Server 22.04 LTS
- `user_data` script to automatically run the panel

After deployment, the panel was available at `http://<PUBLIC_IP>:8501`.

### 🚀 Local Execution

```bash
python -m grpc_services.servidor_grpc
python gateway/gateway_grpc.py
python sensors/sensor_temperatura.py
streamlit run painel/painel.py
```

### ✨ Developed by Bruna Melido and Isadora Lacerda for the Distributed Programming and Cloud Computing courses.