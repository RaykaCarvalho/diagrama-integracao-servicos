# Diagrama de Integração de Serviços

Este projeto representa a arquitetura de um sistema que processa requisições de clientes, simula serviços da AWS, orquestra componentes via containers, coleta métricas da API e exibe dashboards interativos.

## 📊 Diagrama do Sistema

![Diagrama do sistema](diagram/diagrama-integracao-servicos.png)

> **Legenda:** Docker executa o serviço que exibe visualmente os dados.

## 🧩 Componentes do Sistema

- **Cliente que faz requisições**  
  Usuário ou sistema externo que envia solicitações para o serviço.

- **Recebe requisições e responde (FTP Server)**  
  Servidor que recebe requisições do cliente e envia respostas.

- **Simula a AWS e armazena os dados (Amazon DynamoDB)**  
  Banco NoSQL que armazena as informações recebidas, simulando o ambiente da AWS.

- **Orquestra todos os serviços (Container Orchestrator)**  
  Serviço que gerencia e integra todos os componentes da aplicação, garantindo integridade e escalabilidade.

- **Coleta métricas da API**  
  Serviço que monitora acessos à API e armazena métricas em banco de dados.

- **Exibe gráficos e dashboards (Docker)**  
  Interface visual que apresenta os dados coletados em forma de gráficos e painéis interativos.

## 🛠️ Tecnologias Utilizadas

- **Docker** – para empacotamento e execução dos serviços
- **Amazon DynamoDB (simulado)** – armazenamento NoSQL
- **FTP Server (LFTP)** – comunicação com o cliente
- **Orquestrador de Containers** – gerenciamento dos serviços
- **Coletor de Métricas** – monitoramento da API
- **Dashboard** – visualização dos dados

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto