# Documentação Técnica

## Projeto Prático: Plataforma Distribuída de Monitoramento e Controle de Ambientes Inteligentes (Simulada)

**Curso:** Ciência da Computação  
**Disciplina:** Programação Distribuída e Paralela  
**Aluno(a):** Bruna Melido  
**Turma:** [preencher]  
**Bimestre:** 1º  
**Data da entrega:** [preencher]

---

## 1. Visão Geral do Projeto

A "Plataforma SmartCampus" é um sistema distribuído que simula o monitoramento em tempo real de ambientes inteligentes como salas, laboratórios e auditórios universitários. O projeto utiliza tecnologias modernas para integração entre sensores simulados, gateways, microsserviços e uma interface de visualização em tempo real, promovendo escalabilidade, resiliência e interoperabilidade.

---

## 2. Objetivos

- Simular múltiplos ambientes inteligentes em tempo real.
- Garantir comunicação confiável e escalável entre componentes via sockets, gRPC e middleware.
- Implantar o sistema em ambiente cloud (via Streamlit Cloud).
- Exibir as informações via painel de monitoramento visual.

---

## 3. Arquitetura Distribuída

```
Sensor (UDP) 
   ↓
Gateway Simulado (Socket UDP → gRPC) 
   ↓
Microsserviço gRPC (servidor + fila)
   ↓
Armazenamento em arquivo (dados_sensor.txt)
   ↓
Painel Gerencial (Streamlit)
```

---

## 4. Tecnologias Utilizadas

- **Python 3.11**
- **gRPC** para comunicação entre Gateway e Microsserviço
- **Sockets UDP** entre Sensor e Gateway
- **Queue (fila interna)** como Middleware para desacoplamento
- **Streamlit** para o painel gerencial
- **GitHub + Streamlit Cloud** para hospedagem e deploy

---

## 5. Componentes Implementados

### 5.1 Sensor Simulado
Arquivo: `sensors/sensor_temperatura.py`
- Gera valores simulados de temperatura e envia via socket UDP.

### 5.2 Gateway
Arquivo: `gateway/gateway_grpc.py`
- Recebe os dados do sensor via socket UDP.
- Encaminha os dados ao servidor gRPC via protocolo remoto.

### 5.3 Microsserviço gRPC
Arquivos: `grpc_services/`
- `sensor.proto`: definição da interface gRPC
- `servidor_grpc.py`: servidor que recebe os dados e grava no arquivo `dados_sensor.txt`

### 5.4 Middleware
Arquivo: `middleware/fila.py`
- Fila interna com `queue.Queue` para simular Apache Kafka.

### 5.5 Painel Gerencial
Arquivo: `painel/painel.py`
- Interface web com Streamlit para leitura do arquivo de dados.
- Atualiza em tempo real com o último dado recebido.

---

## 6. Execução Local do Projeto

### Requisitos:
- Python 3.11
- streamlit, grpcio, grpcio-tools

### Passos:

1. **Servidor gRPC**  
   `python -m grpc_services.servidor_grpc`

2. **Gateway**  
   `python gateway/gateway_grpc.py`

3. **Sensor**  
   `python sensors/sensor_temperatura.py`

4. **Painel (interface)**  
   `streamlit run painel/painel.py`

---

## 7. Deploy em Cloud

O painel foi publicado utilizando a Streamlit Cloud.  
**Link:** [colocar link do app aqui quando estiver publicado]

---

## 8. Código-Fonte

Disponível em:  
**GitHub:** [https://github.com/brumelido/plataforma-smartcampuss](https://github.com/brumelido/plataforma-smartcampuss)

---

## 9. Conclusão

A plataforma SmartCampus cumpre os requisitos de um sistema distribuído moderno, simulando a interação entre sensores, gateway, microsserviços e interface web. O projeto demonstra conceitos de comunicação assíncrona, escalabilidade e distribuição de responsabilidades de forma eficiente e modular.

---

## 10. Anexos

- Prints das execuções
- Link para o vídeo demonstrativo [adicionar link quando gravado]