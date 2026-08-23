class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_idx in range(numRows):
            
            current_row = [1] * (row_idx + 1)
            
            for col in range(1, row_idx):
                prev_row = triangle[row_idx - 1]
                current_row[col] = prev_row[col - 1] + prev_row[col]
            
            triangle.append(current_row)

        return triangle