import csv
from collections import defaultdict


class BitmapIndex:

    def __init__(self, column_names):
        self.column_names = column_names if isinstance(
            column_names, list) else [column_names]
        self.bitmaps = {col: defaultdict(dict) for col in self.column_names}
        self.unique_values = {col: set() for col in self.column_names}

    def build_index(self, data):
        # Constrói o Bitmap Index para as colunas especificadas.
        for row in data:
            for col in self.column_names:
                value = row[col]
                self.unique_values[col].add(value)
                if value not in self.bitmaps[col]:
                    self.bitmaps[col][value] = [0] * len(data)
                self.bitmaps[col][value][int(row["ID"]) - 1] = 1

    def query(self, column_name, value):
        # Realiza uma consulta no Bitmap Index para um valor específico.
        if column_name in self.bitmaps and value in self.bitmaps[column_name]:
            return self.bitmaps[column_name][value]
        else:
            return [0] * len(self.bitmaps[column_name][next(
                iter(self.bitmaps[column_name]))])

    def compress(self, column_name):
        # Aplica compressão Run-Length Encoding (RLE) nos bitmaps.
        compressed_bitmaps = {}
        for value, bitmap in self.bitmaps[column_name].items():
            compressed_bitmaps[value] = self._run_length_encode(bitmap)
        return compressed_bitmaps

    def _run_length_encode(self, bitmap):
        # Implementa o algoritmo de compressão Run-Length Encoding.
        compressed = []
        count = 1
        for i in range(1, len(bitmap)):
            if bitmap[i] == bitmap[i - 1]:
                count += 1
            else:
                compressed.append((bitmap[i - 1], count))
                count = 1
        compressed.append((bitmap[-1], count))
        return compressed

    def intersect(self, column_name, value1, value2):
        # Realiza a interseção entre dois bitmaps.
        bitmap1 = self.query(column_name, value1)
        bitmap2 = self.query(column_name, value2)
        return [b1 & b2 for b1, b2 in zip(bitmap1, bitmap2)]

    def union(self, column_name, value1, value2):
        # Realiza a união entre dois bitmaps.
        bitmap1 = self.query(column_name, value1)
        bitmap2 = self.query(column_name, value2)
        return [b1 | b2 for b1, b2 in zip(bitmap1, bitmap2)]

    def difference(self, column_name, value1, value2):
        # Realiza a diferença entre dois bitmaps.
        bitmap1 = self.query(column_name, value1)
        bitmap2 = self.query(column_name, value2)
        return [b1 & ~b2 for b1, b2 in zip(bitmap1, bitmap2)]


# Função para carregar dados do CSV
def load_data(filename):
    print("Carregando dados do CSV...")
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        return list(reader)
