import time
from collections import defaultdict
from generate_data import generate_data
from bitmap_index import load_data
from comparison import comparison
from graficos import plot_performance

def main():
  # Gerar dados
  generate_data("data.csv", 1000000)

  # Carregar dados
  data = load_data("data.csv")

  # Comparação de desempenho para busca simples
  comparison(data)

if __name__ == "__main__":
  main()
