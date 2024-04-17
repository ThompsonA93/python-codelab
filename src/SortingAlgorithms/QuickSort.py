data = []
max_elements = 10

for i in range(max_elements):
    value = -i*i
    data.append(value)
    if value % 2 == 0:
        data.append(value)
    

"""
Very simple QuickSort implementation.
Takes a list of integers, returns a sorted list of integers
"""
def quickSort(list: list, lowIndex: int, highIndex: int) -> list:
    if lowIndex < highIndex:
        pi = partition(list, lowIndex, highIndex)
        quickSort(list, lowIndex, pi-1)
        quickSort(list, pi+1, highIndex)
    return list

def partition(subList: list, lowIndex: int, highIndex: int) -> int:
    pivot = subList[highIndex]
    i = lowIndex-1

    for j in range(lowIndex, highIndex):
        if subList[j] <= pivot:
            i = i+1
            (subList[i], subList[j]) = (subList[j], subList[i])

    (subList[i + 1], subList[highIndex]) = (subList[highIndex], subList[i + 1])

    return i+1


print(data)
sortedData = quickSort(data, 0, len(data)-1)
print(sortedData)