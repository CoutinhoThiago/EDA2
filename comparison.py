import time
from bitmap_index import BitmapIndex
from collections import defaultdict
from dicionary import search_dict
from list import search_list


def comparison(data):
    import time
from collections import defaultdict

def search_list(data, column_name, value):
    # Busca em uma lista.
    return [row for row in data if row[column_name] == value]

def search_dict(index, value):
    # Busca em um dicionário.
    return index.get(value, [])

def comparison(data):
    # Criar Bitmap Index
    print("Criar Bitmap Index")
    index = BitmapIndex(["Color", "Letter"])
    index.build_index(data)

    # Criar índice de dicionário
    print("Criar Dicionário")
    dict_index = defaultdict(list)
    for row in data:
        dict_index[row["Color"]].append(row["ID"])

    # Comparação de desempenho para busca simples
    start_time = time.time()
    search_list(data, "Color", "Red")
    list_time = time.time() - start_time

    start_time = time.time()
    search_dict(dict_index, "Red")
    dict_time = time.time() - start_time

    start_time = time.time()
    index.query("Color", "Red")
    bitmap_time = time.time() - start_time

    print("\nComparação de desempenho para busca simples:")
    print(f"Tempo de busca em lista: {list_time:.8f} segundos")
    print(f"Tempo de busca em dicionário: {dict_time:.8f} segundos")
    print(f"Tempo de busca em Bitmap Index: {bitmap_time:.8f} segundos")

    # Determinar o mais rápido na busca simples
    fastest_search = min(list_time, dict_time, bitmap_time)
    if fastest_search == list_time:
        print("O mais rápido na busca simples: Lista")
    elif fastest_search == dict_time:
        print("O mais rápido na busca simples: Dicionário")
    else:
        print("O mais rápido na busca simples: Bitmap Index")

    # Comparação de desempenho para operações de interseção, união e diferença
    start_time = time.time()
    intersection_list = [
        row for row in data
        if row["Color"] == "Red" and row["Letter"] == "A"
    ]
    list_intersection_time = time.time() - start_time

    start_time = time.time()
    intersection_dict = list(set(dict_index["Red"]) & set(dict_index["A"]))
    dict_intersection_time = time.time() - start_time

    start_time = time.time()
    intersection_bitmap = index.intersect("Color", "Letter", "Red", "A")
    bitmap_intersection_time = time.time() - start_time

    start_time = time.time()
    union_list = [
        row for row in data if row["Color"] == "Red" or row["Letter"] == "A"
    ]
    list_union_time = time.time() - start_time

    start_time = time.time()
    union_dict = list(set(dict_index["Red"]) | set(dict_index["A"]))
    dict_union_time = time.time() - start_time

    start_time = time.time()
    union_bitmap = index.union("Color", "Letter", "Red", "A")
    bitmap_union_time = time.time() - start_time

    start_time = time.time()
    difference_list = [
        row for row in data
        if row["Color"] == "Red" and row["Letter"] != "A"
    ]
    list_difference_time = time.time() - start_time

    start_time = time.time()
    difference_dict = list(set(dict_index["Red"]) - set(dict_index["A"]))
    dict_difference_time = time.time() - start_time

    start_time = time.time()
    difference_bitmap = index.difference("Color", "Letter", "Red", "A")
    bitmap_difference_time = time.time() - start_time

    print("\nComparação de desempenho para interseção:")
    print(f"Tempo de interseção em lista: {list_intersection_time:.8f} segundos")
    print(f"Tempo de interseção em dicionário: {dict_intersection_time:.8f} segundos")
    print(f"Tempo de interseção em Bitmap Index: {bitmap_intersection_time:.8f} segundos")

    # Determinar o mais rápido na interseção
    fastest_intersection = min(list_intersection_time, dict_intersection_time, bitmap_intersection_time)
    if fastest_intersection == list_intersection_time:
        print("O mais rápido na interseção: Lista")
    elif fastest_intersection == dict_intersection_time:
        print("O mais rápido na interseção: Dicionário")
    else:
        print("O mais rápido na interseção: Bitmap Index")

    print("\nComparação de desempenho para união:")
    print(f"Tempo de união em lista: {list_union_time:.8f} segundos")
    print(f"Tempo de união em dicionário: {dict_union_time:.8f} segundos")
    print(f"Tempo de união em Bitmap Index: {bitmap_union_time:.8f} segundos")

    # Determinar o mais rápido na união
    fastest_union = min(list_union_time, dict_union_time, bitmap_union_time)
    if fastest_union == list_union_time:
        print("O mais rápido na união: Lista")
    elif fastest_union == dict_union_time:
        print("O mais rápido na união: Dicionário")
    else:
        print("O mais rápido na união: Bitmap Index")

    print("\nComparação de desempenho para diferença:")
    print(f"Tempo de diferença em lista: {list_difference_time:.8f} segundos")
    print(f"Tempo de diferença em dicionário: {dict_difference_time:.8f} segundos")
    print(f"Tempo de diferença em Bitmap Index: {bitmap_difference_time:.8f} segundos")

    # Determinar o mais rápido na diferença
    fastest_difference = min(list_difference_time, dict_difference_time, bitmap_difference_time)
    if fastest_difference == list_difference_time:
        print("O mais rápido na diferença: Lista")
    elif fastest_difference == dict_difference_time:
        print("O mais rápido na diferença: Dicionário")
    else:
        print("O mais rápido na diferença: Bitmap Index")
