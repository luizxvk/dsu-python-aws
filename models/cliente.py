import csv
import os

class Item:
    def __init__(self, codigo, descricao, quantidade, preco_unitario, total_price):
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total_price = total_price

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "descricao": self.descricao,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco_unitario,
            "total_price": self.total_price
        }

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
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "itens": [item.to_dict() for item in self.itens]
        }

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, itens={len(self.itens)})"

    @staticmethod
    def parse_float(value: str) -> float:
        """Converte strings monetárias em float, ex: 'R$4,50' -> 4.5"""
        try:
            if not value:
                return 0.0
            value = str(value).replace('R$', '').replace('.', '').replace(',', '.').strip()
            return float(value)
        except Exception:
            return 0.0

    @staticmethod
    def carregar_de_csv(clientes_csv_path, itens_path_template="data/itens_{id}.csv"):
        clientes = []

        if not os.path.exists(clientes_csv_path):
            raise FileNotFoundError(f"CSV de clientes não encontrado: {clientes_csv_path}")

        with open(clientes_csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for idx, row in enumerate(reader, start=1):
                # ID gerado automaticamente se não existir na planilha
                try:
                    id = int(row.get('id', idx))
                except ValueError:
                    id = idx

                nome = row.get('nome', '').strip()
                email = row.get('email', '').strip()
                telefone = row.get('telefone', '').strip()
                endereco = row.get('endereco', '').strip()

                # Carregar itens do cliente
                itens_csv_path = itens_path_template.format(id=id)
                itens = []

                if os.path.exists(itens_csv_path):
                    with open(itens_csv_path, newline='', encoding='utf-8') as itf:
                        itens_reader = csv.DictReader(itf)
                        for item_row in itens_reader:
                            try:
                                quantidade = int(item_row.get('quantidade', 0))
                                preco_unitario = Cliente.parse_float(item_row.get('preco_unitario', '0'))
                                total_price = Cliente.parse_float(item_row.get('total_price', '0'))

                                itens.append(
                                    Item(
                                        codigo=item_row.get('codigo', '').strip(),
                                        descricao=item_row.get('descricao', '').strip(),
                                        quantidade=quantidade,
                                        preco_unitario=preco_unitario,
                                        total_price=total_price
                                    )
                                )
                            except ValueError as e:
                                print(f"[WARN] Item inválido no cliente {id}: {item_row} -> {e}")

                clientes.append(
                    Cliente(
                        id=id,
                        nome=nome,
                        email=email,
                        telefone=telefone,
                        endereco=endereco,
                        itens=itens
                    )
                )

        return clientes
