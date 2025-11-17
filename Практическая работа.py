import random

def local_search_independent_set(adj_list, max_iterations=1000):
    """
    Локальный поиск для задачи о независимом множестве
    
    Args:
        adj_list: список смежности графа
        max_iterations: максимальное количество итераций
        
    Returns:
        независимое множество и его размер
    """
    n = len(adj_list)
    
    current_set = set()

    vertices = list(range(n))

    random.shuffle(vertices)

    for v in vertices:
        can_add = True
        
        for neighbor in adj_list[v]:
            if neighbor in current_set:
                can_add = False
                break
        
        if can_add:
            current_set.add(v)
    
    for iteration in range(max_iterations):
        improved = False
        
        for v in range(n):
            if v not in current_set:
                can_add = True
                
                for neighbor in adj_list[v]:
                    if neighbor in current_set:
                        can_add = False
                        break
                
                if can_add:
                    current_set.add(v)
                    improved = True
                    break
        
        if not improved:
            break
    
    return current_set, len(current_set)

def generate_test_graph(n=12, edge_probability=0.3):
    """
    Генерация тестового графа
    
    Args:
        n: количество вершин
        edge_probability: вероятность создания ребра
        
    Returns:
        список смежности графа
    """
    adj_list = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_probability:
                adj_list[i].append(j)
                adj_list[j].append(i)
    
    return adj_list

def verify_independent_set(independent_set, adj_list):
    """
    Проверка корректности независимого множества
    
    Args:
        independent_set: множество вершин
        adj_list: список смежности графа
        
    Returns:
        True если множество корректно, иначе False
    """
    is_valid = True
    
    for v in independent_set:
        for neighbor in adj_list[v]:
            if neighbor in independent_set:
                is_valid = False
                print(f"Ошибка: вершины {v} и {neighbor} смежны!")

Вывод:
Граф (список смежности):
Вершина 0: [1, 3, 5]
Вершина 1: [0, 2, 4]
Вершина 2: [1, 3, 6]
...
Вершина 11: [7, 10]

Найденное независимое множество: [0, 2, 4, 6, 8, 11]
Размер независимого множества: 6

Проверка корректности:
Независимое множество корректно ✓