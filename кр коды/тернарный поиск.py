def ternary_search(arr, left, right, x):
    if right >= left:
        # Вычисляем две точки деления
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        # Проверяем, не нашли ли элемент
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        
        # Определяем, в какой трети искать
        if x < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, x)
        elif x > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, x)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, x)
    
    return -1

def ternary_search_iterative(arr, x):
    """Итеративная версия тернарного поиска"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        
        if x < arr[mid1]:
            right = mid1 - 1
        elif x > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
print(f"Массив: {arr}")
print(f"Рекурсивный поиск {target}: индекс {ternary_search(arr, 0, len(arr)-1, target)}")
print(f"Итеративный поиск {target}: индекс {ternary_search_iterative(arr, target)}")

Вывод:
Массив: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Рекурсивный поиск 6: индекс 5
Итеративный поиск 6: индекс 5
