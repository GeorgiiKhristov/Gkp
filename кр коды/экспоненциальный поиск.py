def binary_search(arr, left, right, x):
    """Вспомогательная функция бинарного поиска"""
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    
    # Если элемент в начале
    if arr[0] == x:
        return 0
    
    # Находим диапазон для бинарного поиска
    i = 1
    while i < n and arr[i] <= x:
        i *= 2
    
    # Выполняем бинарный поиск в найденном диапазоне
    return binary_search(arr, i // 2, min(i, n - 1), x)

# Пример использования
arr = [2, 3, 4, 10, 40, 45, 50, 60, 70, 80, 90, 100]
target = 45
print(f"Массив: {arr}")
print(f"Поиск {target}: индекс {exponential_search(arr, target)}")


Вывод:
Массив: [2, 3, 4, 10, 40, 45, 50, 60, 70, 80, 90, 100]
Поиск 45: индекс 5