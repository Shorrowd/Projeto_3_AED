import random
import time
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.setrecursionlimit(1000000)

#CREDITS: "https://www.geeksforgeeks.org/python-program-for-insertion-sort/"

def insertion_sort(arr):
    # percorre a lista a partir do segundo elemento
    for i in range(1, len(arr)):
        # vai ao elemento selecionado e vai comparar com os da esquerda se os elem da esquerda forem maiores troca
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  #  desloca os elementos maiores para a direita
            j -= 1
        arr[j + 1] = key

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

tamanhos = [10000, 20000, 30000, 50000, 100000]
resultados = {"A": [], "B": [], "C": []}

# main
for tamanho in tamanhos:
    A, B, C = gerar_listas(tamanho)
    for nome, lista in zip(["A", "B", "C"], [A, B, C]):
        tempo = medir_tempo(insertion_sort, lista)
        resultados[nome].append(tempo)
        print(f"Tamanho {tamanho}, Conjunto {nome}: {tempo:.3f}s")

# Regressão n^2
plt.figure(figsize=(10, 6))
for nome, cor in zip(["A", "B", "C"], ["blue", "green", "red"]):
    x = np.array(tamanhos)
    y = np.array(resultados[nome])

    coeffs = np.polyfit(x ** 2, y, 1)
    fit_fn = np.poly1d(coeffs)

    plt.plot(x, y, "o", label=f"Dados {nome}", color=cor)
    plt.plot(x, fit_fn(x ** 2), "--", label=f"Ajuste n^2 {nome}", color=cor)

plt.title("Regressão n^2 do Tempo de Execução - Insertion Sort")
plt.xlabel("Tamanho da Lista (n)")
plt.ylabel("Tempo de Execução (segundos)")
plt.ylim(0)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()