data = [5, 3, 2, 4, 6, 9, 8, 10, 0, 12, 15, 22, 23, 56, 43]

"""
Short implementation of linear searching.
Returns element on success, -1 on failure
"""
def linearSearch(element: int) -> int:
    for values in data:
        if(element == values):
            return element
    return -1

if __name__ == "__main__":
    print("Lookup:", linearSearch(9))
    print("Lookup:", linearSearch(55))
    print("Lookup:", linearSearch(43))



