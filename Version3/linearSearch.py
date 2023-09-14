def linearSearch(list, target):
    for i in range(len(list)):
        if (target == list[i]):
            return i
    return -1


list = [23, 4235, 64, 344, 89, 34, 22, 44, ]
print(linearSearch(list, 344))
