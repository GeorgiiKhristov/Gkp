import math

def jump_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    
    # Определяем размер прыжка
    step = int(math.sqrt(n))
    prev = 0
    
    # Прыжки для нахождения диапазона
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Линейный поиск в найденном диапазоне
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    
    return -1

# Пример использования
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
target = 55
print(f"Массив: {arr}")
print(f"Поиск {target}: индекс {jump_search(arr, target)}")

Вывод:

Массив: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
Поиск 55: индекс 10