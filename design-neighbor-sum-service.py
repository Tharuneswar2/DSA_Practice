class NeighborSumService:
    def __init__(self, grid):
        """
        Initialize the NeighborSumService with a grid of integers.
        
        Args:
        grid (list of lists): A 2D grid of integers.
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.cache = {}

    def get_neighbor_sum(self, row, col):
        """
        Get the sum of the neighboring cells of the cell at (row, col).
        
        Args:
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
        Returns:
        int: The sum of the neighboring cells.
        """
        # Check if the result is already cached
        if (row, col) in self.cache:
            return self.cache[(row, col)]

        # Initialize the sum to 0
        neighbor_sum = 0

        # Check all neighboring cells
        for r in range(max(0, row-1), min(self.rows, row+2)):
            for c in range(max(0, col-1), min(self.cols, col+2)):
                # Skip the cell itself
                if r == row and c == col:
                    continue
                # Add the value of the neighboring cell to the sum
                neighbor_sum += self.grid[r][c]

        # Cache the result
        self.cache[(row, col)] = neighbor_sum

        return neighbor_sum


# Example usage
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
service = NeighborSumService(grid)
print(service.get_neighbor_sum(1, 1))  # Output: 30