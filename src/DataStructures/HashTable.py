
class HashTable:
    """
    Very simple Hashtable implementation. Does not handle collisions.
    
    Attributes:
    ----------
    data: dict
        Dictionary containing data entries. Keys are hashed, values are non-hashed
    data_max_length: int
        Value limiting the maximum size of dictionary

    Methods:
    --------
    hash_fn(value: int) -> int
        Hashes integer value following remainder method
    insert(value: int) -> None
        Inserts value into table given index of hash_fn(value)
    search(value: int) -> int
        Looksup and returns value from table given index of hash_fn(value). Does not remove the value from the table
    delete(value: int) -> None
        Deletes value from table given index of hash_fn(value).
    """

    def __init__(self, max_length: int):
        self.data = {}
        self.data_max_lenght = max_length

    def hash_fn(self, value: int) -> int:
        return value % self.data_max_lenght
    
    def insert(self, value: int) -> None:
        self.data[self.hash_fn(value)] = value

    def search(self, value: int) -> int:
        return self.data[self.hash_fn(value)]

    def delete(self, value: int) -> None:
        self.data.pop(self.hash_fn(value))
    

if __name__ == "__main__":
    """
    Kurze Testsequenz des programmierten Hashtables:
    """
    ht = HashTable(8)

    ht.insert(12)
    ht.insert(24)
    ht.insert(35)
    print(ht.data)

    print("Searching:",ht.search(12))
    print("Searching:",ht.search(24))
    print("Searching:",ht.search(35))

    ht.delete(12)
    print(ht.data)