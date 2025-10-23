# DSU-Python-AWS

**DSU-Python-AWS** (Documento de Saída do Usuário) é uma aplicação Python que automatiza a geração de PDFs a partir de dados de clientes armazenados em arquivos CSV. O projeto é pensado para execução em **AWS Lambda** utilizando **Docker**, com armazenamento em **S3** e monitoramento via **CloudWatch**.

---

## 🚀 Funcionalidades

- Carregar CSV de clientes do S3
- Carregar CSV de itens de cada cliente
- Preencher template HTML com dados do cliente
- Gerar PDF utilizando **WeasyPrint**
- Salvar PDF no bucket de **output** do S3
- Logs detalhados de cada etapa no **CloudWatch**

---

## 🏗 Arquitetura
CSV (input) ──► Lambda (Docker) ──► PDF ──► S3 (output)


**Componentes:**

- **Lambda Function**: Processa arquivos CSV e gera PDFs.
- **Buckets S3**:
  - `dsu-python-aws/input` → Recebe arquivos CSV de clientes
  - `dsu-python-aws/output` → Armazena PDFs gerados
- **Docker**: Contêiner Python 3.11 com dependências (Jinja2, WeasyPrint, boto3)
- **CloudWatch**: Monitoramento de logs e métricas da execução

---

## 🗂 Estrutura do Projeto

dsu-python-aws/
│
├── main.py # Script principal / Lambda handler
├── Dockerfile # Configuração do container
├── requirements.txt # Dependências Python
├── templates/
│ └── cliente_template.html # Template HTML para gerar PDF
├── data/
│ └── clientes.csv # CSV de exemplo
├── controllers/
│ └── pdf_controller.py # Lógica de geração de HTML/PDF
├── models/
│ └── cliente.py # Classes Cliente e Item
└── output/ # PDFs gerados localmente (opcional)


---

## ⚙ Pré-requisitos

- Docker >= 24
- AWS CLI configurado
- Permissões AWS:
  - `s3:GetObject`
  - `s3:PutObject`
  - `logs:CreateLogGroup`
  - `logs:CreateLogStream`
  - `logs:PutLogEvents`
- Python 3.11 (local, se for testar sem Docker)

---

## 💻 Setup Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/dsu-python-aws.git
   cd dsu-python-aws

2 Criar e ativar ambiente virtual:

python -m venv venv
source venv/bin/activate


3 Instalar dependências:

pip install --upgrade pip
pip install -r requirements.txt


4 Testar localmente:

python main.py

PDFs serão gerados na pasta output/.


⚠️ Observações

WeasyPrint precisa de bibliotecas nativas (cairo, pango, gdk-pixbuf) no Lambda Docker.

CSV deve ter cabeçalhos esperados.

Template HTML pode ser customizado conforme identidade visual da empresa.

O projeto suporta clientes sem itens; nesses casos, a tabela ficará vazia.

🔗 Referências

WeasyPrint

Jinja2

AWS Lambda Container

AWS S3

AWS CloudWatch

👤 Autor

Luiz – Desenvolvedor de soluções backend, automação e cloud computing