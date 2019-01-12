import numpy
import random
import time
from PIL import Image


# 0 is free cells, 1 is wall cells and 0.5 is visited cells
class Maze:
    # width and height are in cells while cell_size is in pixel.
    def __init__(self, width=100, height=50, cell_size=10,
                 free_cell_color=(255, 255, 255),
                 visited_cell_color=(0, 0, 255),
                 wall_cell_color=(0, 0, 0)):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.free_cell_color = free_cell_color
        self.visited_cell_color = visited_cell_color
        self.wall_cell_color = wall_cell_color
        self.cells = numpy.ones((self.height, self.width))

    def color_cell(self, cell):
        color = None
        if self.cells[cell] == 0:
            color = self.free_cell_color
        if self.cells[cell] == 0.5:
            color = self.visited_cell_color
        if self.cells[cell] == 1:
            color = self.wall_cell_color
        return color

    def change_cell(self, cell, value):
        self.cells[cell] = value
    
    def draw_my_maze(self):
        img = Image.new( 'RGB', (self.height+1, self.width+1), "black") # Create a new black image
        pixels = img.load() # Create the pixel map
        #img.show()
        for cell in numpy.ndindex(self.height, self.width):
            #print((tuple(self.cell_size * c for c in cell)[::-1]), self.color_cell(cell) )
            #print(cell[0], cell[1])
            if self.color_cell(cell)[2] != 0 :
                pixels[cell[0]+1,cell[1]+1] = (255, 255, 255)
        #img.show()
        img.save('result.bmp')


    #################################################################################################################
    #                                               DFS GENERATION                                                  #
    #################################################################################################################

    def unvisited_cell_neighbors(self, cell):
        neighbors = []
        west = []
        north = []
        east = []
        south = []
        if cell[1] > 1 and self.cells[cell[0], cell[1] - 2] == 1:
            west.extend([(cell[0], cell[1] - 1), (cell[0], cell[1] - 2)])
        if cell[1] < self.width - 2 and self.cells[cell[0], cell[1] + 2] == 1:
            east.extend([(cell[0], cell[1] + 1), (cell[0], cell[1] + 2)])
        if cell[0] > 1 and self.cells[cell[0] - 2, cell[1]] == 1:
            north.extend([(cell[0] - 1, cell[1]), (cell[0] - 2, cell[1])])
        if cell[0] < self.height - 2 and self.cells[cell[0] + 2, cell[1]] == 1:
            south.extend([(cell[0] + 1, cell[1]), (cell[0] + 2, cell[1])])
        neighbors.extend([west, north, east, south])
        neighbors = [x for x in neighbors if x != []]
        return neighbors


    def dfs(self):
        visited = []
        current_cell = (0, 0)
        visited.append(current_cell)
        self.change_cell(current_cell, 0)

        while visited:
            neighbors = self.unvisited_cell_neighbors(current_cell)
            if neighbors:
                next_cell = random.choice(neighbors)
                self.change_cell(next_cell[0], 0)
                self.change_cell(next_cell[1], 0)
                visited.extend([next_cell[0], next_cell[1]])
                current_cell = next_cell[1]
            else:
                if len(visited) > 1:
                    self.change_cell(visited[-1], 0.5)
                    del visited[-1]
                    self.change_cell(visited[-1], 0.5)
                    del visited[-1]
                    current_cell = visited[-1]
                else:
                    self.change_cell(visited[-1], 0.5)
                    current_cell = visited[-1]
                    del visited[-1]
			

# To have a borderless maze, chose an odd width and height
maze = Maze(90, 10, 8)
maze.dfs()
maze.draw_my_maze()
  

