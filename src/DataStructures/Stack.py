class Stack:
    """
    Stack (de. Kellerstapel): Eine abstrakte Datenstruktur zum Speichern von Daten.
    Basiert auf Last-in-First-Out Prinzip, d.h. das letzte gespeicherte Element wird als erstes wieder betrachtet.
    
    Attributes:
    ----------
    data: Array vom Typ int.

    Methods:
    --------
    push(value) : 
        Füge neues Element 'value' dem Stack hinzu.
    pop : int
        Entnehme ein Element dem Stack und gebe es zurück.
    peek : int
        Betrachte ein Element vom Stack und gebe es zurück. Entnimmt das Element nicht.
    isEmpty : bool
        Gebe zurück ob der Stack leer ist. Gebe True zurück wenn leer, andernfalls False.
    isFull : bool
        Gebe zurück ob der Stack voll ist. Gebe True zurück wenn voll, andernfalls False.
    """
    data = []

    def push(self, value: int) -> None:
        self.data.append(value)

    def pop(self) -> int:
        return self.data.pop()

    def peek(self) -> int:
        return self.data[len(self.data)-1]

    def isEmpty(self) -> bool:
        if not self.data:
            return True
        else:
            return False



if __name__ == "__main__":
    """
    Kurze Testsequenz des programmierten Stacks:
    - Check ob Leer
    - Push von Elementen
    - Check ob Leer
    - Pop von Elementen
    - Check ob Leer
    """
    s = Stack()
    print("Stack is empty:", s.isEmpty())

    s.push(5)
    print("Peeking on Stack:", s.peek())

    s.push(10)
    print("Peeking on Stack:", s.peek())

    s.push(15)
    print("Peeking on Stack:", s.peek())

    print("Stack is empty:", s.isEmpty())

    print("Poping from Stack:", s.pop())
    print("Poping from Stack:", s.pop())
    print("Poping from Stack:", s.pop())

    print("Stack is empty:", s.isEmpty())