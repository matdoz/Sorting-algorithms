def quickSort(list):
    if len(list) > 1:
        pivot = list[-1]
        left = []
        right = []
        for i in range(len(list) - 1):
            if list[i] < pivot:
                left.append(list[i])
            else:
                right.append(list[i])
        quickSort(left)
        left.append(pivot)
        list[:] = left
        quickSort(right)
        list[:] += right
        return list


if __name__ == '__main__':
    inputList = [0, 19, 1, 13, 5, 64, 57, 2]
    print('Input')
    print(inputList, end="\n\n")
    inputList = quickSort(inputList)
    print('Output')
    print(inputList, end="\n\n")
