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
def countingSort(input: list) -> list:
    # Count the occurence of each element
    entries = {}
    for i in input:
        if i not in entries.keys():
            entries[i] = 1
        else:
            entries[i] = entries.get(i) + 1
    
    # Sort dictionary by keys
    print(entries)
    entries = sorted(entries.items())
    print(entries)

    # Convert dictionary-content to array
    #   keys depict what is appended
    #   value depicts how often it is appended
    data_entries = []
    for entry in entries:                   # Get Touple: (-81, 1)
        for x in range(entry[1]):           # Get range of 2nd element: 1
            data_entries.append(entry[0])   # Append value of 1 element

    return data_entries

print(data)
sortedData = countingSort(data)
print(sortedData)