'''
Inspiration from this source: https://www.geeksforgeeks.org/merge-sort/
'''


def mergeSort(list, length):
    if len(list) > 1:
        left = list[:len(list)//2]
        mergeSort(left, len(left))
        right = list[len(list)//2:]
        mergeSort(right, len(right))
        i = j = k = 0
        while i < length:
            if k < len(right) and j < len(left) and left[j] > right[k]:
                list[i] = right[k]
                k += 1
            elif j < len(left):
                list[i] = left[j]
                j += 1
            else:
                list[i] = right[k]
                k += 1
            i += 1
        return list


if __name__ == '__main__':
    inputList = [0, 19, 1, 13, 5, 64, 57]
    print('Input')
    print(inputList, end="\n\n")
    inputList = mergeSort(inputList, len(inputList))
    print('Output')
    print(inputList, end="\n\n")
