def BubbleSort(inputList):
    swap = True
    while swap:
        swap = False
        for i in range(len(inputList)):
            if i < (len(inputList) - 1) and inputList[i] > inputList[i + 1]:
                swap = True
                tmp = inputList[i]
                inputList[i] = inputList[i + 1]
                inputList[i + 1] = tmp
    return inputList


inputList = [8, 9, 1, 9, 8, 6, 5, 3, 2, 1]
print(BubbleSort(inputList))
