import random

# 1. Vytvoření pole s 10 přeházenými hodnotami od 0 do 100
array = random.sample(range(101), 10)
print("Původní pole:", array)

# 2. Implementace bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Pokud je prvek větší než následující, prohoďte je
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 3. Implementace bogo sort
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:  # Pokud je prvek větší než následující
            return False  # Pokud není pole seřazeno
    return True  # Pokud je pole seřazeno
        

def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)  # Náhodně promíchá pole
    return arr

# 4. Implementace selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 5. Implementace insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Třídění pomocí jednotlivých algoritmů
print("Bubble sort:", bubble_sort(array.copy()))
print("Bogo sort:", bogo_sort(array.copy()))
print("Selection sort:", selection_sort(array.copy()))
print("Insertion sort:", insertion_sort(array.copy()))
