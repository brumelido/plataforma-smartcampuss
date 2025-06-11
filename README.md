Bruna Melido
brumelido
Em voz

⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 27/03/2025 19:29
https://docs.google.com/document/d/1Nd2LXw7N88JFnEz6XF-nTSFqq11ymJ1Zx8BZrGen77o/edit?usp=sharing
Pode mudar o q vc achar melhor
Bruna Melido — 27/03/2025 19:30
ta certo, obgg
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 31/03/2025 08:03
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import desenhar_cubo

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    glRotatef(5, 0, 1, 0)  # Rotação para a esquerda
                if evento.key == K_RIGHT:
                    glRotatef(-5, 0, 1, 0)  # Rotação para a direita

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        desenhar_cubo()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if name == "main":
    main()
Bruna Melido — 09/04/2025 11:50
https://drive.google.com/drive/folders/1mzIzhlZZliffBoVZKcyl8jIm_A_bteXg?usp=sharing
Google Drive: Sign-in
Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).
Bruna Melido — 16/04/2025 22:42
oeee
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 22:42
oiii
já já eu volto
Bruna Melido — 16/04/2025 22:42
okay
q call morta mds
sol falando morrendo
netao sla
shopp tb
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 22:45
avisa lá no wpp
Bruna Melido — 16/04/2025 22:45
robertino.... nem fala sla
dudu entrou
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 22:58
vcs já entraram?
Bruna Melido — 16/04/2025 22:58
nao sei, to resolvendo um negocio aqui
ja entrou?
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 23:10
ainda não
mas podem ir jogando qualquer coisa; eu já já volto
Bruna Melido — 16/04/2025 23:11
to meio ocupada aqui ainda
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 23:20
n tou mto legal
:/ acho q vou dormir em breve
Bruna Melido — 16/04/2025 23:20
pouxa (nao tava c vontade de jogar mesmo
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 23:21
tudo bem ent!! jogamos outro momento
Bruna Melido — 16/04/2025 23:21
espero que fique tudo bem dorinha
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 23:21
obg bruna
vou amanhã sim
Bruna Melido — 16/04/2025 23:21
to aqui qualquer coisa
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 16/04/2025 23:21
vamos juntas
se animar um pouco
Bruna Melido — 16/04/2025 23:21
vamos
bjood
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 30/04/2025 18:08
alou
Bruna Melido — 30/04/2025 18:08
to ligando o note
Bruna Melido
 iniciou uma chamada que durou uma hora. — 30/04/2025 18:11
Bruna Melido — 30/04/2025 18:57
https://meet.google.com/kwm-yniz-fuv
Meet
Real-time meetings by Google. Using your browser, share your video, desktop, and presentations with teammates and customers.
Imagem
Bruna Melido — 13/05/2025 07:58
Imagem
o q vc acha?
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 13/05/2025 07:59
gostei, mas e aquilo da tinta que vc disse?
Bruna Melido — 13/05/2025 07:59
vou mandar msg perguntando m
posso mandar no grupo la?
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 13/05/2025 07:59
sim
Bruna Melido — 13/05/2025 07:59
ok
Bruna Melido — 13/05/2025 09:03
Tipo de arquivo em anexo: acrobat
OKETÁ Tijolo Amazônico - Placas dos materiais.pdf
129.88 KB
plaquinha pra colocar nas coisas
ta meio feia ainda
Bruna Melido — 03/06/2025 12:41
📢 Foi dada a largada! 🏁

Já está aberta a votação para o prêmio de Popularidade do Amazon Hacking 2024! 😱

♻️ E nós da startup Arandu Technology estamos concorrendo com o projeto Oketá: proposta da primeira usina de biometano no Pará, transformando o lixo em combustível verde para os barcos das ilhas do estado! ⛵️🌱

Gostaríamos muito do apoio de vocês 🫵🏼 nessa etapa para tornar esse sonho realidade!

Para votar OKÉTA! 👇🏽
https://amazonhacking.com.br/pt/solutions

Centro Universitário do Estado do Pará - CESUPA

Time: 
Amanda Klautau
Bruna Melido
Isadora Lacerda
Gabriel Lopes
Gabriel Normando
Lucas Augusto
Tiago Miranda 
Yohan Marçal

Enviado automaticamente
Amazon Hacking
Amazon Hacking
O Amazon Hacking é um programa de formação para alunos da Escola de Negócios, Tecnologia e Inovação do CESUPA - ARGO, que visa conectar empresas comprometidas com a sustentabilidade amazônica, a comunidade local e seu conhecimento tradicional, junto ao conhecimento científico e tecnológico em prol do desenvolvimento bioeconômico da ...
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 09:20
# CloudFormation Template - SmartCampus

AWSTemplateFormatVersion: '2010-09-09'
Description: >
  Infraestrutura AWS para a Plataforma SmartCampus. Cria VPC, Subnet, EC2 com Streamlit e Bucket S3.
Expandir
smartcampus-stack.yaml
3 KB
Bruna Melido — 09:28
oie
ta ai
https://github.com/brumelido/plataforma-smartcampuss.git
GitHub
GitHub - brumelido/plataforma-smartcampuss
Contribute to brumelido/plataforma-smartcampuss development by creating an account on GitHub.
GitHub - brumelido/plataforma-smartcampuss
⋆𐙚₊ 𝐼𝘴𝘢 ˚⊹♡ — 09:47
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