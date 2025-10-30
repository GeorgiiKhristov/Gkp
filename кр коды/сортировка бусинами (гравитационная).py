def bead_sort(arr):
    if not arr or min(arr) < 0:
        raise ValueError("Массив должен содержать неотрицательные числа")
    
    # Создаем "абак" - матрицу бусин
    max_val = max(arr)
    abacus = [[0] * len(arr) for _ in range(max_val)]
    
    # Размещаем бусины
    for i, num in enumerate(arr):
        for j in range(num):
            abacus[j][i] = 1
    
    # Симулируем падение бусин
    for i in range(max_val):
        # Считаем количество бусин в ряду
        bead_count = sum(abacus[i])
        # Опускаем бусины
        for j in range(len(arr)):
            abacus[i][j] = 1 if j < bead_count else 0
    
    # Преобразуем обратно в числа
    result = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(max_val):
            result[i] += abacus[j][i]
    
    return result

# Пример использования
arr = [3, 1, 4, 1, 5]
print("Исходный массив:", arr)
print("Отсортированный массив:", bead_sort(arr.copy()))


Вывод:
Исходный массив: [3, 1, 4, 1, 5]
Отсортированный массив: [5, 4, 3, 1, 1]