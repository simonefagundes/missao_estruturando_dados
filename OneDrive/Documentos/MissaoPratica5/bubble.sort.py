def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if j>j+1:
                valorJ = array[j]
                array[j] = array[j+1]
                array[j+1] = valorJ
arrayNumerico = [1,10,12,16,18,14,22,26,29,35,34,51,56,41,44]
bubbleSort(arrayNumerico)
print(arrayNumerico)
    
