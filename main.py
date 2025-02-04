import time
from collections import defaultdict
from generate_data import generate_data
from bitmap_index import load_data, BitmapIndex
from comparison import comparison
from graficos import plot_performance


def main():
  # Gerar dados
  generate_data("data10.csv", 10)
  generate_data("data.csv", 1000000)
  
  # Carregar dados
  data10 = load_data("data10.csv")
  data = load_data("data.csv")

  # Cria o Bitmap Index para as colunas especificadas
  column_names = ["Letter"]  
  bitmap_index = BitmapIndex(column_names)
  bitmap_index.build_index(data10)

  # Exemplo de consulta
  column_name = "Letter"
  value = "A"
  print(f"Bitmap para '{value}' na coluna '{column_name}':")
  print(bitmap_index.query(column_name, value))

  # Exemplo de compressão
  print(f"Bitmap comprimido para '{value}' na coluna '{column_name}':")
  print(bitmap_index.compress(column_name))

  # Exemplo de interseção
  value1 = "A"
  value2 = "B"
  print(f"Interseção entre '{value1}' e '{value2}':")
  print(bitmap_index.intersect(column_name, value1, value2))

  # Exemplo de união
  print(f"União entre '{value1}' e '{value2}':")
  print(bitmap_index.union(column_name, value1, value2))

  # Exemplo de diferença
  print(f"Diferença entre '{value1}' e '{value2}':")
  print(bitmap_index.difference(column_name, value1, value2))

  # EXEMPLO COMPLEXO DE COMPARAÇÃO

  # Comparação de desempenho para busca simples
  comparison(data)


if __name__ == "__main__":
  main()
