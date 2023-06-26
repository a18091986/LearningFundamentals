def maximum_selection_sort(arr: list) -> None:
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
