class Vertex:
    """
    Vertex: Einzelner Punkt eines Graphen

    Attribute:
    ----------
    id: int
        Nummer zur eindeutigen Identifikation eines Vertex
    edge: array
        Liste aller verbundenen Vertices

    Methods:
    getId: int
        Gibt die ID des Vertex zurück
    addEdge: None
        Fügt einen Link zu einem Vertex hinzu
    getEdges: list[int]
        Gibt eine Liste aller Links zu allen verbunden Vertices zurück
    -------- 
    """
    def __init__(self, id: int):
        self.id = id
        self.edges = []

    def getId(self) -> int:
        return self.id

    def addEdge(self, edge: int) -> None:
        if edge not in self.edges:
            self.edges.append(edge)

    def getEdges(self) -> list:
        return self.edges

class Graph:
    """
    Graph: Eine weitere Datenstruktur zum Speichern von Daten.
    Daten werden in Form von Vertices gespeichert (siehe Klasse 'Vertex')
    
    Die Implementierung dieser Klasse basiert auf einem ungewichteten, ungerichteten Graphen-
    D.h.:
    - Verbindungen zwischen Daten sind sowohl von A nach B, als auch von B nach A.
    - Verbindungen besitzen keine Kosten. 

    Attributes:
    ----------
    vertices: dict
        Ein dictionary aller Knoten des Graphes

    Methods:
    --------
    addVertice: None
        Fügt dem Graphen einen Knoten hinzu.
    getVertices: dict
        Gibt ein dict aller Knoten des Graphen zurück
    linkVertices: None
        Erzeugt eine neue Verbindung zwischen zwei Knoten

    """
    def __init__(self):
        self.vertices = {}

    def addVertice(self, vertice: Vertex) -> None:
        self.vertices[vertice.id] = vertice
    
    def getVertices(self) -> dict:
        return self.vertices
    
    def linkVertices(self, v1: Vertex, v2: Vertex) -> None:
        self.vertices[v1.id].addEdge(v2.id)
        self.vertices[v2.id].addEdge(v1.id)

if __name__ == "__main__":
    """
    Kurze Testsequenz des programmierten Graphen:
    """ 
    v1 = Vertex(0)
    v2 = Vertex(1)
    v3 = Vertex(2)
    v4 = Vertex(3)
    v5 = Vertex(4)        

    print("V0 Edges:", v1.getEdges())
    print("V1 Edges:", v2.getEdges())
    print("V2 Edges:", v3.getEdges())
    print("V3 Edges:", v4.getEdges())
    print("V4 Edges:", v5.getEdges())

    g = Graph()
    g.addVertice(v1)
    g.addVertice(v2)
    g.addVertice(v3)
    g.addVertice(v4)
    g.addVertice(v5)

    print("G Vertices:", g.getVertices().keys())

    g.linkVertices(v1, v2)
    g.linkVertices(v1, v3)
    g.linkVertices(v1, v5)
    g.linkVertices(v2, v4)
    g.linkVertices(v2, v5)
    g.linkVertices(v3, v4)
    g.linkVertices(v4, v5)

    print("V0 Edges:", v1.getEdges())
    print("V1 Edges:", v2.getEdges())
    print("V2 Edges:", v3.getEdges())
    print("V3 Edges:", v4.getEdges())
    print("V4 Edges:", v5.getEdges())


