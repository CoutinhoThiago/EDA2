import csv
import random


# Função para gerar dados aleatórios
def generate_data(filename, num_rows):
    # Definindo categorias para demonstrar vantagens e desvantagens do Bitmap Index
    colors = ["Red", "Green", "Blue", "Yellow", "Black", "White"]
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = [random.randint(1, 100) for _ in range(num_rows)]

    # Gerando dados aleatórios
    data = []
    for i in range(num_rows):
        row = {
            "ID": i + 1,
            "Color": random.choice(
                colors
            ),  # Categoria com baixa cardinalidade (ótimo para Bitmap Index)
            "Letter":
            random.choice(letters),  # Categoria com média cardinalidade
            "Number": numbers[
                i]  # Categoria com alta cardinalidade (não ideal para Bitmap Index)
        }
        data.append(row)

    # Salvando os dados em um arquivo CSV
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file,
                                fieldnames=["ID", "Color", "Letter", "Number"])
        writer.writeheader()
        writer.writerows(data)

    print(f"Dados gerados e salvos em {filename}")
