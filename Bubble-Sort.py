def bubbleSort(list):
    swap = True
    while swap:
        swap = False
        for i in range(len(list)):
            if i < (len(list) - 1) and list[i] > list[i + 1]:
                swap = True
                tmp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = tmp
    return list


if __name__ == '__main__':
    inputList = [8, 9, 1, 9, 8, 6, 5, 3, 2, 1]
    print('Input:')
    print(inputList, end="\n\n")
    inputList = bubbleSort(inputList)
    print('Output:')
    print(inputList, end="\n\n")
