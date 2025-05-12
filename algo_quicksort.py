import random
import time
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.setrecursionlimit(1000000)

#CREDITS: "https://www.geeksforgeeks.org/quick-sort-algorithm/"

def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    meio = (low + high) // 2

    # Ordena os três elementos
    if arr[low] > arr[meio]:
        arr[low], arr[meio] = arr[meio], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[meio] > arr[high]:
        arr[meio], arr[high] = arr[high], arr[meio]

    pivot_value = arr[meio]

    # troca
    arr[meio], arr[high] = arr[high], arr[meio]
    i = low

    # Items Trocas
    for j in range(low, high):
        if arr[j] <= pivot_value:
            arr[i], arr[j] = arr[j], arr[i] #troca
            i += 1

    # troca
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low, high):
    while low < high:
        # insertion sort para arrays menores
        if high - low + 1 < 1000:
            insertion_sort(arr, low, high)
            return

        # divide o array e obtem a posição correta do pivô
        pi = partition(arr, low, high)

        # recursão  
        if pi - low < high - pi:
            quickSort(arr, low, pi - 1)
            low = pi + 1   # atualiza os limites para continuar no lado direito
        else:
            quickSort(arr, pi + 1, high)
            high = pi - 1   # atualiza os limites para continuar no lado esquerdo

def gerar_listas(tamanho):
    num_repetidos = int(tamanho * 0.05)

    A = list(range(1, tamanho + 1))
    indices = random.sample(range(1, tamanho), num_repetidos)
    for idx in indices:
        A[idx] = A[idx - 1]

    B = list(range(tamanho, 0, -1))
    indices = random.sample(range(1, tamanho), num_repetidos)
    for idx in indices:
        B[idx] = B[idx - 1]

    C = list(range(1, tamanho + 1))
    indices = random.sample(range(1, tamanho), num_repetidos)
    for idx in indices:
        C[idx] = C[idx - 1]
    random.shuffle(C)

    return A, B, C

def medir_tempo(algoritmo, arr):
    arr_copy = arr.copy()
    inicio = time.time()

    algoritmo(arr_copy, 0, len(arr_copy) - 1)

    fim = time.time()    
    return fim - inicio

tamanhos = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
resultados = {"A": [], "B": [], "C": []}

# main
for tamanho in tamanhos:
    A, B, C = gerar_listas(tamanho)
    for nome, lista in zip(["A", "B", "C"], [A, B, C]):
        tempo = medir_tempo(quickSort, lista)
        resultados[nome].append(tempo)
        print(f"Tamanho {tamanho}, Conjunto {nome}: {tempo:.3f}s")

# Regressão n log n 
plt.figure(figsize=(10, 6))
for nome, cor in zip(["A", "B", "C"], ["blue", "green", "red"]):
    x = np.array(tamanhos)
    y = np.array(resultados[nome])

    n_log_n = x * np.log2(x)

    coeffs = np.polyfit(n_log_n, y, 1)
    fit_fn = np.poly1d(coeffs)

    plt.plot(x, y, "o", label=f"Dados {nome}", color=cor)
    plt.plot(x, fit_fn(n_log_n), "--", label=f"Ajuste n log n {nome}", color=cor)

plt.title("Regressão n log n do Tempo de Execução - Quick Sort")
plt.xlabel("Tamanho da Lista (n)")
plt.ylabel("Tempo de Execução (segundos)")
plt.ylim(0)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
