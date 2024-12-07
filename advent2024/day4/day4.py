def read_grid(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]

# def find_xmas(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     count = 0
    
#     # All 8 possible directions
#     directions = [
#         (0, 1),   # right
#         (0, -1),  # left
#         (1, 0),   # down
#         (-1, 0),  # up
#         (1, 1),   # diagonal down-right
#         (-1, -1), # diagonal up-left
#         (1, -1),  # diagonal down-left
#         (-1, 1)   # diagonal up-right
#     ]
    
#     def check_direction(x, y, dx, dy):
#         if not (0 <= x + 3*dx < rows and 0 <= y + 3*dy < cols):
#             return False
#         word = ''
#         for i in range(4):
#             word += grid[x + i*dx][y + i*dy]
#         return word == 'XMAS'
    
#     for i in range(rows):
#         for j in range(cols):
#             for dx, dy in directions:
#                 if check_direction(i, j, dx, dy):
#                     count += 1
                    
#     return count

# def main():
#     grid = read_grid('input.txt')
#     result = find_xmas(grid)
#     print(f"Found {result} instances of XMAS")

# if __name__ == '__main__':
#     main()

def find_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def is_mas(word):
        return word in ['MAS', 'SAM']
    
    def check_x_pattern(i, j):
        # Check if we can form complete X pattern
        if not (0 <= i-1 < rows and 0 <= i+1 < rows and 
                0 <= j-1 < cols and 0 <= j+1 < cols):
            return False
            
        # Get the two diagonal strings
        diagonal1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]  # top-left to bottom-right
        diagonal2 = grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1]  # top-right to bottom-left
        
        # Check if both diagonals form MAS (in either direction)
        return (is_mas(diagonal1) and is_mas(diagonal2))
    
    # Check each possible center point of X
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if check_x_pattern(i, j):
                count += 1
                
    return count

# Test
if __name__ == "__main__":
    grid = read_grid("input.txt")
    result = find_x_mas(grid)
    print(f"Number of X-MAS patterns found: {result}")