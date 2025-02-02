import matplotlib.pyplot as plt  # Adicionando matplotlib para gráficos

def plot_performance(times, labels, title):
  # Plota um gráfico de barras comparando os tempos de execução.
  plt.bar(labels, times)
  plt.xlabel('Método')
  plt.ylabel('Tempo (segundos)')
  plt.title(title)
  plt.show()