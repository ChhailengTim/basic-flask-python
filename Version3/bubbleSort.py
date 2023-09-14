def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


def insertionSort(list):
    for i in range(len(list)):
        j = i
        while j > 0 and list[j] < list[j - 1]:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
        return list


list = [323, 35, 64, 3, 55, 6775, 34, 342, 62, ]
print(bubbleSort(list))
print(insertionSort(list))
