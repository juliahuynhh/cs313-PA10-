import unittest 
from ImageGraph import ColorVertex, ImageGraph
from test import create_graph  

class TestGraphAlgos(unittest.TestCase): 

    def initiate_graph(self, file): 
        in_data = open(file)
        data = in_data.read()   
        graph, search_start, search_color = create_graph(data)
        return graph, search_start, search_color

    def indices_convert(self, vertex_list): 
        indices = []
        for vertex in vertex_list: 
            indices.append(vertex.index)
        return indices 

    def test_bfs_on_image(self): 
        """ #name(Image BFS) #score(10)"""
        expected_recur = [2, 1, 5, 0, 9, 3, 8, 7, 10]
        expected_iter = [2, 5, 1, 9, 0, 8, 3, 7, 10]


    def test_dfs_on_image(self): 
        """#name(Image DFS) #score(10)"""
        expected_recur = [2, 1, 0, 3, 7, 8, 9, 5, 10]
        expected_iter = [2, 5, 9, 8, 7, 10, 3, 0, 1]
        graph, search_start, search_color = self.initiate_graph('image.in')
        result = graph.bfs(search_start, search_color) 
        actual = self.indices_convert(result) 

        if graph.dfs_method == 'recursive': 
            pass 

        if graph.dfs_method == 'iterative': 
            pass 


    def test_bfs_on_heart(self): 
        pass 

    def test_dfs_on_heart(self): 
        pass 

    def test_bfs_on_small(self): 
        pass 

    def test_dfs_on_small(self): 
        pass