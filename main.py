from controllers.pdf_controller import PDFController
from models.cliente import Cliente
from datetime import datetime
import os

# DSU - Documento de Saída de Usuário

# Para AWS Lambda
try:
    import boto3
    LAMBDA = True
except ImportError:
    LAMBDA = False

s3 = boto3.client("s3") if LAMBDA else None

def processar_clientes(local_csv, template_path, output_dir, output_bucket=None):
    os.makedirs(output_dir, exist_ok=True)

    clientes = Cliente.carregar_de_csv(local_csv)

    for cliente in clientes:
        dados_cliente = {
            "company_name": "Minha Empresa",
            "report_title": "Relatório de Cliente",
            "client_name": cliente.nome,
            "client_id": cliente.email,
            "client_address": cliente.endereco,
            "items": [
                {
                    "code": item.codigo,
                    "description": item.descricao,
                    "quantity": item.quantidade,
                    "unit_price": item.preco_unitario,
                    "total_price": item.total_price
                } for item in cliente.itens
            ],
            "generation_date": datetime.now().strftime("%d/%m/%Y")
        }

        output_html_path = os.path.join(output_dir, f"cliente_{cliente.id}.html")
        output_pdf_path = os.path.join(output_dir, f"cliente_{cliente.id}.pdf")

        filled_html = PDFController.gerar_html(template_path, dados_cliente, output_html_path)
        PDFController.gerar_pdf(filled_html, output_pdf_path)

        print(f"PDF gerado com sucesso: {output_pdf_path}")

        # Se for Lambda, envia para S3
        if LAMBDA and output_bucket:
            s3.upload_file(output_pdf_path, output_bucket, f"output/cliente_{cliente.id}.pdf")
            print(f"PDF enviado para S3: {output_bucket}/output/cliente_{cliente.id}.pdf")

# -----------------------
# Executar local
# -----------------------
def main():
    local_csv = "data/clientes.csv"
    template_path = "templates/cliente_template.html"
    output_dir = "output"
    processar_clientes(local_csv, template_path, output_dir)

# -----------------------
# Handler Lambda
# -----------------------
def lambda_handler(event, context):
    # Espera bucket + key no evento
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    local_csv = f"/tmp/{os.path.basename(key)}"
    output_dir = "/tmp/output"
    template_path = "/var/task/templates/cliente_template.html"  # no container Lambda

    # Baixa CSV do S3
    s3.download_file(bucket, key, local_csv)

    output_bucket = bucket  # mesmo bucket, mas grava em 'output/'
    processar_clientes(local_csv, template_path, output_dir, output_bucket)

    return {
        "statusCode": 200,
        "body": f"PDFs gerados com sucesso a partir de {key}"
    }

if __name__ == "__main__":
    main()
