import pygame

class Grid:
    def __init__(self):
        self.grid_rows = 20
        self.grid_columns = 10
        self.gridMatrix = [[0 for j in range(self.grid_columns)] for i in range(self.grid_rows)]
        self.grid_dimensions = 30
        self.grid_colors = self.get_grid_colors  


    def print_grid(self): 
        for i in range(self.grid_rows):
            for x in range(self.grid_columns):
                print(self.gridMatrix[i][x],end = " ")    
            print()  

    def get_grid_colors():
        red = (255,0,0) 
        green = (0,255,0)  
        blue = (0,0,255)   
        cyan = (0, 255, 255)  
        yellow = (255, 255, 0)
        purple = (128, 0, 128)
        orange = (255, 127, 0)


        return [red,green,blue,cyan,yellow,purple,orange]     

    def draw(self,screen): 
        for rows in range(self.grid_rows):
            for columns in range(self.grid_columns):
                cell_value = self.gridMatrix[rows][columns]
                rect_block = pygame.Rect((columns * self.grid_dimensions)+20,(rows * self.grid_dimensions)+20,
                                        self.grid_dimensions,self.grid_dimensions )   
                pygame.draw.rect(screen,(31,31,31),rect_block,1)






