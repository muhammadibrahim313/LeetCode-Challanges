class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        def rotate(matrix):
            """Rotate the matrix 90 degrees clockwise."""
            # Transpose
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # Reverse rows
            for row in matrix:
                row.reverse()
        
        # Check all 4 rotations
        for _ in range(4):
            if mat == target:
                return True
            rotate(mat)
        
        return False
