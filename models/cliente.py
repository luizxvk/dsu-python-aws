import csv
import os

class Item:
    def __init__(self, codigo, descricao, quantidade, preco_unitario, total_price):
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total_price = total_price

class Cliente:
    def __init__(self, id, nome, email, telefone, endereco, itens):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.itens = itens

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco
        }

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, email={self.email}, telefone={self.telefone}, endereco={self.endereco}, itens={len(self.itens)})"

    @staticmethod
    def carregar_de_csv(clientes_csv_path, itens_path_template="data/itens_{id}.csv"):
        clientes = []
        with open(clientes_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for idx, row in enumerate(reader, start=1):
                id = idx  # gera ID automaticamente se não tiver na planilha

                # Carregar itens do cliente
                itens_csv_path = itens_path_template.format(id=id)
                itens = []
                if os.path.exists(itens_csv_path):
                    with open(itens_csv_path, newline='', encoding='utf-8') as itf:
                        itens_reader = csv.DictReader(itf)
                        for item_row in itens_reader:
                            itens.append(
                                Item(
                                    codigo=item_row.get('codigo', ''),
                                    descricao=item_row.get('descricao', ''),
                                    quantidade=int(item_row.get('quantidade', 0)),
                                    preco_unitario=item_row.get('preco_unitario', '0'),
                                    total_price=item_row.get('total_price', '0')
                                )
                            )

                clientes.append(
                    Cliente(
                        id=id,
                        nome=row.get('nome', ''),
                        email=row.get('email', ''),
                        telefone=row.get('telefone', ''),
                        endereco=row.get('endereco', ''),
                        itens=itens
                    )
                )
        return clientes
