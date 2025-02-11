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
  
  column_names2= ["Color", "Letter"]  
  bitmap_index2 = BitmapIndex(column_names2)
  bitmap_index2.build_index(data10)
  
  print("Criar Bitmap Index\n")
  
  # Exemplo de consulta
  column_name1 = "Letter"
  value1 = "A"
  print(f"Bitmap para '{value1}' na coluna '{column_name1}':")
  print(bitmap_index.query(column_name1, value1), "\n")
  
  # Exemplo de compressão
  print(f"Bitmap comprimido da coluna '{column_name1}':")
  print(bitmap_index.compress(column_name1), "\n")
  
  # Exemplo de interseção
  column_name2 = "Color"
  value2 = "Red"
  print(f"Interseção entre '{value1}' e '{value2}':")
  print(bitmap_index2.intersect(column_name1, column_name2, value1, value2), "\n")
  
  # Exemplo de união
  print(f"União entre '{value1}' e '{value2}':")
  print(bitmap_index2.union(column_name1, column_name2, value1, value2), "\n")
  
  # Exemplo de diferença
  print(f"Diferença entre '{value1}' e '{value2}':")
  print(bitmap_index2.difference(column_name1, column_name2, value1, value2), "\n")
  # EXEMPLO COMPLEXO DE COMPARAÇÃO

  # Comparação de desempenho para busca simples
  comparison(data)


if __name__ == "__main__":
  main()
