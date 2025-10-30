def flip(arr, i):
    """Переворачивает массив от 0 до i"""
    start = 0
    while start < i:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
        i -= 1

def find_max_index(arr, n):
    """Находит индекс максимального элемента в массиве"""
    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def pancake_sort(arr):
    n = len(arr)
    curr_size = n
    
    while curr_size > 1:
        # Находим индекс максимального элемента
        max_index = find_max_index(arr, curr_size)
        
        # Если максимальный элемент не на своем месте
        if max_index != curr_size - 1:
            # Переворачиваем до максимального элемента
            if max_index != 0:
                flip(arr, max_index)
            # Переворачиваем весь текущий сегмент
            flip(arr, curr_size - 1)
        
        curr_size -= 1
    
    return arr

# Пример использования
arr = [23, 10, 20, 11, 12, 6, 7]
print("Исходный массив:", arr)
print("Отсортированный массив:", pancake_sort(arr.copy()))


Вывод:
Исходный массив: [23, 10, 20, 11, 12, 6, 7]
Отсортированный массив: [6, 7, 10, 11, 12, 20, 23]