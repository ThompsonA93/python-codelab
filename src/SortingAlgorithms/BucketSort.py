data = []
max_elements = 10

for i in range(max_elements):
    value = -i*i
    data.append(value)
    if value % 2 == 0:
        data.append(value)
    

"""
Very simple CountingSort implementation.
Takes a list of integers, returns a sorted list of integers
"""
def bucketSort(list: list) -> list:
    bucket = []
    
    # TODO 

    return bucket
        

print(data)
sortedData = bucketSort(data)
print(sortedData)