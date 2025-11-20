def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    result = []
    last_end = -1
    
    for start, end in intervals:
        if start >= last_end:
            result.append([start, end])
            last_end = end
    
    return result

print("Введите количество интервалов:")
n = int(input().strip())

intervals = []
print("Введите интервалы в формате 'start end':")
for i in range(n):
    data = input().split()
    start = int(data[0])
    end = int(data[1])
    intervals.append([start, end])

result = interval_scheduling(intervals)

print("\nРезультат:")
print("Выбранные интервалы:", result)
print("Количество выбранных интервалов:", len(result))

Вывод:
Введите количество интервалов:
3
Введите интервалы в формате 'start end':
1 5
2 4
6 9

Результат:
Выбранные интервалы: [[2, 4], [6, 9]]
Количество выбранных интервалов: 2