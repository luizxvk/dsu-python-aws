from jinja2 import Environment, FileSystemLoader, select_autoescape
try:
    from weasyprint import HTML
except ImportError:
    HTML = None
import os

class PDFController:

    @staticmethod
    def gerar_html(template_path, dados_cliente, output_path=None):
        # Criar ambiente Jinja2
        env = Environment(
            loader=FileSystemLoader(os.path.dirname(template_path)),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template(os.path.basename(template_path))
        filled_html = template.render(dados_cliente)

        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(filled_html)

        return filled_html

    @staticmethod
    def gerar_pdf(filled_html, output_pdf_path):
        if HTML is None:
            raise RuntimeError(
                "WeasyPrint não está instalado. Instale com: pip install weasyprint"
            )
        HTML(string=filled_html).write_pdf(output_pdf_path)
