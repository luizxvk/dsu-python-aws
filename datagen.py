import csv

# Defina quantos itens quer gerar
num_itens = 50
arquivo_saida = "data/itens_2.csv"

with open(arquivo_saida, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["codigo", "descricao", "quantidade", "preco_unitario", "total_price"])

    for i in range(1, num_itens + 1):
        codigo = f"{i:03d}"
        descricao = f"Produto {chr(64 + ((i-1) % 26) + 1)}"  # vai de A a Z e repete
        quantidade = (i % 5) + 1  # 1 a 5
        preco_unitario = (i * 3) % 50 + 1  # preço entre 1 e 50
        total_price = quantidade * preco_unitario
        writer.writerow([codigo, descricao, quantidade, f"R${preco_unitario},00", f"R${total_price},00"])

print(f"CSV com {num_itens} itens gerado em {arquivo_saida}")
