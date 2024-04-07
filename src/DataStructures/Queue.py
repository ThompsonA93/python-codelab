class Queue:
    """
    Queue (de. Warteschlange): Eine abstrakte Datenstruktur zum Speichern von Daten.
    Basiert auf Last-in-Last-Out Prinzip, d.h. das letzte gespeicherte Element wird als letztes wieder betrachtet.
    
    Attribute:
    ----------
    data: Array vom Typ int.

    Methods:
    --------
    enqueue(value) : 
        Füge neues Element 'value' der Queue hinzu.
    dequeue : int
        Entnehme ein Element von der Queue und gebe es zurück.
    front : int
        Betrachte das erste Element der Queue und gebe es zurück. Entnimmt das Element nicht.
    rear : int
        Betrachte das letzte Element der Queue und gebe es zurück. Entnimmt das Element nicht.
    isEmpty : bool
        Gebe zurück ob die Queue leer ist. Gebe True zurück wenn leer, andernfalls False.
    """
    data = []

    def enqueue(self, value: int) -> None:
        self.data.append(value)

    def dequeue(self) -> int:
        return self.data.pop(0)

    def front(self) -> int:
        return self.data[0]

    def rear(self) -> int:
        return self.data[len(self.data)-1]

    def count(self) -> int:
        return len(self.data)

    def isEmpty(self) -> bool:
        if not self.data:
            return True
        else:
            return False



if __name__ == "__main__":
    """
    Kurze Testsequenz der programmierten Queue:
    - Check ob Leer
    - Enqueue von Elementen
    - Check auf Anzahl der Elemente
    - Dequeue von Elementen
    - Check ob Leer
    """
    s = Queue()

    print("Queue is empty:", s.isEmpty())

    s.enqueue(5)
    s.enqueue(10)
    print("Front, Rear: ", (s.front(), s.rear()))

    s.enqueue(15)
    s.enqueue(20)
    print("Front, Rear: ", (s.front(), s.rear()))

    print("Counting elements:", s.count())

    print("Dequeue: ", s.dequeue())
    print("Front, Rear: ", (s.front(), s.rear()))

    print("Dequeue: ", s.dequeue())
    print("Front, Rear: ", (s.front(), s.rear()))

    print("Dequeue: ", s.dequeue())
    print("Front, Rear: ", (s.front(), s.rear()))

    print("Dequeue: ", s.dequeue())
    print("Queue is empty:", s.isEmpty())
