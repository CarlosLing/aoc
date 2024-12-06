import numpy as np
from typing import List

class AOCMatrix():

    def __init__(self, data:List[str]):
        self.data = data
        self.matrix = [[y for y in x] for x in self.data]

    def get_matrix(self):
        return self.matrix
    
    

    def get_diagonals(self):
        diagonals = []
        n, m = len(self.matrix), len(self.matrix[0])
        
        # Get all diagonals from bottom-left to top-right
        for p in range(n + m - 1):
            diagonal = []
            for q in range(max(0, p - m + 1), min(p + 1, n)):
                diagonal.append(self.matrix[q][p - q])
            diagonals.append(diagonal)
        
        # Get all anti-diagonals from top-left to bottom-right
        for p in range(n + m - 1):
            anti_diagonal = []
            for q in range(max(0, p - m + 1), min(p + 1, n)):
                anti_diagonal.append(self.matrix[q][m - 1 - (p - q)])
            diagonals.append(anti_diagonal)
        
        return diagonals

    def rotate_matrix(self):
        self.matrix = np.rot90(self.matrix)
        
    def transpose_matrix(self):
        self.matrix = np.transpose(self.matrix)
    
    def __str__(self):
        matrix_str = "\n".join(["".join([str(x) for x in row]) for row in self.matrix])
        return matrix_str