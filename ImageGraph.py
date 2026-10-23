import os
import sys
from Stack import Stack
from Queue import Queue

# -----------------------PRINTING LOGIC, DON'T CHANGE ----------------------------

# this enables printing colors on Windows somehow
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"

# Input: text is some string we want to write in a specific color
#   color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
    color = color.strip().lower()
    if not color in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text

# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
    print(colored(BLOCK_CHAR, color)*2, end='')

# -----------------------PRINTING LOGIC END ---------------------------


# DO NOT CHANGE THE ColorVertex CLASS
class ColorVertex:
    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    # add_edge: add an edge to the ColorVertex that maps to index
    def add_edge(self, vertex_index):
        self.edges.append(vertex_index)

    # visit_and_set_color: used when traversing this ColorVertex
    # as part of a bucket fill request
    # sets visited to True and updates color
    def visit_and_set_color(self, color):
        self.visited = True
        self.prev_color = self.color
        self.color = color

        print("Visited vertex " + str(self.index))


class ImageGraph:
    def __init__(self, image_size):
        self.vertexes = []
        self.image_size = image_size

    # print_image: prints the image formed by the vertexes on the command line
    def print_image(self):
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for vertex in self.vertexes:
            img[vertex.y][vertex.x] = vertex.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    # reset_visited: sets the visited flag to False for all vertexes
    def reset_visited(self):
        for i in range(len(self.vertexes)):
            self.vertexes[i].visited = False

    def print_adjacency_matrix(self):
        print("Adjacency matrix:")
        # If you find it helpful to print the adjacency matrix, you can do so here

        # Leave this print in to give space after the adjacency matrix
        print()

    # Purpose: gets the vertex associated with a given vertex index 
    # Input: vertex_index - the index of a vertex 
    # Output: vertex - the vertex associated with the given vertex index 
    def get_vertex(self, vertex_index): 
        for vertex in self.vertexes: 
            if vertex.index == vertex_index: 
                return vertex

        return None 
    
    def bfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting BFS; initial state:")
        self.print_image()

        ### MY CODE ####
        start_vertex = self.get_vertex(start_index)
        vertex_queue = Queue()
        visited = []
        vertex_queue.enqueue(start_vertex)
        visited.append(start_vertex)

        while vertex_queue.size() > 0: 
            current_vertex = vertex_queue.dequeue() 
            current_vertex.visit_and_set_color(color) 
            self.print_image()

            for vertex_index in current_vertex.edges:
                vertex = self.get_vertex(vertex_index) 
                if vertex not in visited: 
                    vertex_queue.enqueue(vertex)
                    visited.append(vertex)
        return visited 


    def dfs(self, start_index, color):
        # reset visited status
        self.reset_visited()
        # print initial state
        print("Starting DFS; initial state:")
        self.print_image()

        ### MY CODE ###

        vertex_stack = Stack() 
        visited = [] 
        start_vertex = self.get_vertex(start_index)
        vertex_stack.push(start_vertex)
        visited.append(start_vertex)

        while vertex_stack.size() > 0: 
            current_vertex = vertex_stack.pop() 
            if current_vertex not in visited: 
                visited.append(current_vertex)
            for vertex_label in current_vertex.edges: 
                vertex = self.get_vertex(vertex_label)
                if vertex not in visited: 
                    vertex_stack.push(vertex)
    
        for vertex in visited: 
            vertex.visit_and_set_color(color) 
            self.print_image() 
        return visited 




