"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        """
        Add a vertex to the graph.
        """
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices: # v1 = vertex 1 / v2 = vertex 2 etc
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("Error! The vertex doesn't exist.")
        """
        Add a directed edge to the graph.
        """
    def bft(self, starting_vertex): # Bredth First Traversal
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue() # An empty Queue (keeps track of order to be printed)
        visited = set() # A set for visited
        q.enqueue(starting_vertex) # Add starting_vertex to Queue

        while q.size():
            vertex = q.dequeue() # dequeue the first item in the q
            if vertex not in visited:
                print(vertex) # Print vertex
                # print("-----------------------------")
                visited.add(vertex) # Mark node as visited
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        q.enqueue(neighbor) # Add neighbor to q
        return visited

    def dft(self, starting_vertex): # Depth First Traversal
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack() # An empty Stack (keeps track of order to be printed)
        visited = set() # A set for visited
        s.push(starting_vertex)

        while s.size():
            vertex = s.pop() # The value of the starting node
            if vertex not in visited: 
                print(vertex) # Print vertex
                # print("*******************************")
                visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    s.push(neighbor)
        return visited

    def dft_recursive(self, starting_vertex, visited=None): # Depth First Traversal
        if visited is None:
            visited = set() # A set for visited

        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                print("\n")
                print(vertex) # Print vertex
                print("*******************************")
                visited.add(vertex)
                self.dft_recursive(vertex, visited)

            return visited
   
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
    def bfs(self, starting_vertex, destination_vertex): # Bredth First Search
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
    def dfs(self, starting_vertex, destination_vertex): # Depth First Search
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
