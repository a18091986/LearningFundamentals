# ---------------------------------------------------------------------------------------------------------------------
# сортировка кучей (пирамидальная сортировка)
# ---------------------------------------------------------------------------------------------------------------------
# каждый массив является двоичным деревом
# чтобы такое дерево стало "кучей" каждый потомок должен быть больше родителя (максимальная куча)

def heap_sort(arr: list) -> None:
    arr_len = len(arr)

    # создаем максимальную кучу из первоначального массива
    for i in range(arr_len // 2 - 1, -1, -1):
        heapify(arr, arr_len, i)

    for i in range(arr_len - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    # превращает бинарное дерево в максимальную кучу
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# ---------------------------------------------------------------------------------------------------------------------
# сортировка выбором
# ---------------------------------------------------------------------------------------------------------------------

def selection_sort(arr: list) -> None:
    # метод сортировки поиском максимума. сложность алгоритма - квадратичная
    # O(N^2).
    # Нестабильный алгоритм - т.е. если есть равные элементы - они могут поменяться местами
    down_max_element(arr, 0, len(arr))
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_max_element(arr, 0, i)


def down_max_element(arr: list, start_index: int, end_index: int):
    # находит максимальный элемент и помещает его в начало массива
    index_of_max_element = start_index
    for i in range(start_index, end_index):
        if arr[index_of_max_element] < arr[i]:
            index_of_max_element = i
    arr[start_index], arr[index_of_max_element] = arr[index_of_max_element], arr[start_index]
