import random
import time
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.setrecursionlimit(1000000)

#CREDITS: "https://www.geeksforgeeks.org/python-program-for-heap-sort/"

def heapify(arr, n, i):
    largest = i    #pai
    l = 2 * i + 1  #esquerda    
    r = 2 * i + 2  #direita

    #se o filho esquerdo for maior que o pai
    if l < n and arr[i] < arr[l]:
        largest = l

    #se o filho direito for maior que o pai
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # troca

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # controi max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # Heap sort
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # troca
        heapify(arr, i, 0) 


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

    algoritmo(arr_copy)

    fim = time.time()    
    return fim - inicio

tamanhos = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
resultados = {"A": [], "B": [], "C": []}

# main
for tamanho in tamanhos:
    A, B, C = gerar_listas(tamanho)
    for nome, lista in zip(["A", "B", "C"], [A, B, C]):
        tempo = medir_tempo(heapSort, lista)
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

plt.title("Regressão n log n do Tempo de Execução - Heap Sort")
plt.xlabel("Tamanho da Lista (n)")
plt.ylabel("Tempo de Execução (segundos)")
plt.ylim(0)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()