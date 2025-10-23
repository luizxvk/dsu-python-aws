# DSU-Python-AWS 

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**DSU-Python-AWS** é uma aplicação Python que gera PDFs automaticamente a partir de CSVs de clientes, ideal para rodar em **AWS Lambda** com **Docker**, salvando arquivos no **S3** e registrando logs no **CloudWatch**.

---

##  Funcionalidades

- Carregar CSV de clientes e itens do S3  
- Preencher **template HTML** com dados do cliente  
- Gerar PDF com **WeasyPrint**  
- Salvar PDFs no bucket de **output** do S3  
- Logs detalhados no **CloudWatch**  

---

##  Arquitetura
CSV (input) ──► Lambda (Docker) ──► PDF ──► S3 (output)


**Componentes:**

- **Lambda Function**: processa CSV e gera PDFs  
- **Buckets S3**:  
  - `input/` → CSVs de clientes  
  - `output/` → PDFs gerados  
- **Docker**: Python 3.11 + dependências (`WeasyPrint`, `Jinja2`, `boto3`)  
- **CloudWatch**: logs e métricas  

---

##  Estrutura do Projeto

dsu-python-aws/
├─ main.py # Lambda handler
├─ Dockerfile # Container config
├─ requirements.txt # Dependências Python
├─ templates/
│ └─ cliente_template.html
├─ data/
│ └─ clientes.csv # CSV de exemplo
├─ controllers/
│ └─ pdf_controller.py
├─ models/
│ └─ cliente.py
└─ output/ # PDFs gerados localmente (opcional)

---

##  Pré-requisitos

- Docker >= 24  
- Python 3.11 (local)  
- AWS CLI configurado  
- Permissões AWS:  
  - `s3:GetObject` / `s3:PutObject`  
  - `logs:CreateLogGroup` / `CreateLogStream` / `PutLogEvents`  

---

##  Setup Local (Passo a Passo)



```bash
1️ Clonar o repositório
git clone https://github.com/seuusuario/dsu-python-aws.git
cd dsu-python-aws

2️ Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate

3️ Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

4️ Testar localmente
python main.py
PDFs serão gerados na pasta output/.
```

### Observações

WeasyPrint precisa de bibliotecas nativas (cairo, pango, gdk-pixbuf) no Docker Lambda

CSV deve ter cabeçalhos corretos

Template HTML pode ser customizado

Clientes sem itens → tabela vazia

### Referências

WeasyPrint
Jinja2
AWS Lambda Container
AWS S3
AWS CloudWatch

👤 Autor

Luiz – Backend, automação e cloud computing
