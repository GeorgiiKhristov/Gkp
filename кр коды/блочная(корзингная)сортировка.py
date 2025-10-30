def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Создаем корзины
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # Распределяем элементы по корзинам
    max_val = max(arr)
    for num in arr:
        index = min(n - 1, int(num * n / (max_val + 1)))
        buckets[index].append(num)
    
    # Сортируем каждую корзину
    for bucket in buckets:
        bucket.sort()
    
    # Объединяем корзины
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result

# Пример использования
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Исходный массив:", arr)
print("Отсортированный массив:", bucket_sort(arr))

Вывод:
Исходный массив: [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
Отсортированный массив: [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]