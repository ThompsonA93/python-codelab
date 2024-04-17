data = []
max_elements = 10

for i in range(max_elements):
    value = -i*i
    data.append(value)


"""
Very simple BubbleSort implementation.
Takes a list of integers, returns a sorted list of integers
"""
def bubbleSort(input: list) -> list:
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i] < input[j]:
                tmp = input[i]
                input[i] = input[j]
                input[j] = tmp
    return input

print(data)
sortedData = bubbleSort(data)
print(sortedData)