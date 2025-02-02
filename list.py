def search_list(data, column_name, value):
  # Busca em uma lista.
  return [row for row in data if row[column_name] == value]