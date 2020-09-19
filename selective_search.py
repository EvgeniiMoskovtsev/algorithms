from random import randint


def search_index(unsorted_array):
    index = 0
    temp = unsorted_array[index]
    for i in range(1, len(unsorted_array)):
        if unsorted_array[i] <= temp:
            temp = unsorted_array[i]
            index = i
    return index


def selective_search(unsorted_array):
    sorted_array = []
    for i in range(len(unsorted_array)):
        index = search_index(unsorted_array)
        sorted_array.append(unsorted_array.pop(index))
    return sorted_array


if __name__ == "__main__":
    list_array = []
    for i in range(10):
        list_array.append(randint(0, 10))
    print(list_array)
    sorted_array = selective_search(list_array)
    print(sorted_array)