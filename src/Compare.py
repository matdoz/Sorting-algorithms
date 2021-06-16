import timeit
import matplotlib.pyplot as plt
from Bubble_Sort import bubbleSort
from Merge_Sort import mergeSort
from Quick_Sort import quickSort
inputList = [8, 9, 1, 9, 8, 6, 5, 3, 2, 1, 57, 13, 23, 1, 123, 9, 1, 9, 8, 6,
             5, 3, 2, 1, 57, 13, 23, 1, 123, 9, 1, 9, 8, 6, 5, 3, 2, 1, 57, 13, 23, 1, 123, 3, 2, 1, 57, 13, 23, 1, 123, 9, 1, 9, 8, 6, 5, 3, 2, 1, 57, 13, 23, 1, 123, 3, 2, 1, 57, 13, 23, 1, 123, 9, 1, 9, 8, 6, 5, 3, 2, 1, 57, 13, 23, 1, 123, 3, 2, 1, 57, 13, 23, 1, 123, 9, 1, 9, 8, 6, 5, 3, 2, 1, 57, 13, 23, 1, 123, 3, 2, 1, 57, 13, 23, 1, 123]
lengthInput = len(inputList)
loops = 1000
quickTime = timeit.timeit('quickSort(inputList.copy())',
                          'from __main__ import quickSort, inputList', number=loops)/loops
bubbleTime = timeit.timeit('bubbleSort(inputList.copy())',
                           'from __main__ import bubbleSort, inputList', number=loops)/loops
mergeTime = timeit.timeit('mergeSort(inputList.copy(), lengthInput)',
                          'from __main__ import mergeSort, inputList, lengthInput', number=loops)/loops
left = [1, 2, 3]
height = [bubbleTime, mergeTime, quickTime]
label = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
plt.title('Length of array: ' + str(lengthInput) +
          '  Measurements: ' + str(loops))
plt.ylabel('seconds')
plt.gcf().canvas.set_window_title('Comparison of sorting algorithms')
plt.bar(left, height, tick_label=label,
        width=0.8, color=['blue', 'red', 'green'])
plt.show()
