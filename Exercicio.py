import time
import numpy as np
import pandas as pd

# Função Merge Sort
def merge_sort(arr, count):
    if len(arr) <= 1:
        return arr, count

    mid = len(arr) // 2
    left, count = merge_sort(arr[:mid], count)
    right, count = merge_sort(arr[mid:], count)
    
    return merge(left, right, count)

def merge(left, right, count):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        count += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result, count

# Função maxVal1 (iterativa)
def max_val1(arr):
    max_val = arr[0]
    count = 0
    for i in range(1, len(arr)):
        count += 1
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val, count

# Função maxVal2 (recursiva - divisão e conquista)
def max_val2(arr, init, end, count):
    if init == end:
        return arr[init], count+1
    
    mid = (init + end) // 2
    v1, count = max_val2(arr, init, mid, count)
    v2, count = max_val2(arr, mid+1, end, count)
    
    return max(v1, v2), count+1

# Função Multiplication (Divisão e Conquista)
def multiply(x, y, n, count):
    if n == 1:
        return x * y, count+1
    
    m = (n + 1) // 2
    a = x >> m
    b = x & ((1 << m) - 1)
    c = y >> m
    d = y & ((1 << m) - 1)

    e, count = multiply(a, c, m, count)
    f, count = multiply(b, d, m, count)
    g, count = multiply(b, c, m, count)
    h, count = multiply(a, d, m, count)

    result = (1 << (2 * m)) * e + (1 << m) * (g + h) + f
    return result, count+1

# Teste e coleta de dados
sizes = [32, 2048, 1048576]  # Tamanhos dos vetores
results = []

for size in sizes:
    # Gerar vetor aleatório
    arr = np.random.randint(1, 100000, size)
    
    # Merge Sort
    start_time = time.time()
    _, iterations = merge_sort(arr.copy(), 0)
    end_time = time.time()
    results.append(["Merge Sort", size, iterations, end_time - start_time])
    
    # Max Val 1 (Iterativo)
    start_time = time.time()
    _, iterations = max_val1(arr.copy())
    end_time = time.time()
    results.append(["MaxVal1 (Iterativo)", size, iterations, end_time - start_time])
    
    # Max Val 2 (Recursivo)
    start_time = time.time()
    _, iterations = max_val2(arr.copy(), 0, len(arr) - 1, 0)
    end_time = time.time()
    results.append(["MaxVal2 (Recursivo)", size, iterations, end_time - start_time])

# Teste Multiplicação Inteira
bit_sizes = [4, 16, 64]

for bits in bit_sizes:
    max_val = (1 << bits) - 1  # Valor máximo suportado pelos bits
    x = np.random.randint(1, max_val, dtype=np.uint64)
    y = np.random.randint(1, max_val, dtype=np.uint64)
    
    start_time = time.time()
    _, iterations = multiply(int(x), int(y), bits, 0)  # Convertendo para int padrão do Python
    end_time = time.time()
    
    results.append(["Multiplicação Inteira", bits, iterations, end_time - start_time])
 
# Criar DataFrame e exibir resultados
df_results = pd.DataFrame(results, columns=["Algoritmo", "Tamanho", "Iterações", "Tempo (s)"])
print(df_results)