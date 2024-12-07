# def parse_map(input_text):
#     return [list(line) for line in input_text.strip().splitlines()]

# def get_start_position(grid):
#     for y in range(len(grid)):
#         for x in range(len(grid[0])):
#             if grid[y][x] == '^':
#                 return (x, y)
#     return None

# def is_valid_position(pos, grid):
#     x, y = pos
#     return 0 <= y < len(grid) and 0 <= x < len(grid[0])

# def get_next_position(pos, direction):
#     x, y = pos
#     dx, dy = direction
#     return (x + dx, y + dy)

def solve_part1(input_text):
    # Parse input
    grid = parse_map(input_text)
    pos = get_start_position(grid)
    
    # Direction vectors: up, right, down, left
    directions = [
        (0, -1),  # up
        (1, 0),   # right
        (0, 1),   # down
        (-1, 0)   # left
    ]
    
    current_dir = 0
    visited = set([pos])
    
    while True:
        next_pos = get_next_position(pos, directions[current_dir])
        
        if not is_valid_position(next_pos, grid):
            break
            
        x, y = next_pos
        if grid[y][x] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            pos = next_pos
            visited.add(pos)
            
    return len(visited)

# # Read input from file
# def main():
#     with open('input.txt', 'r') as file:
#         input_text = file.read()
    
#     result = solve_part1(input_text)
#     print(f"Guard visits {result} distinct positions")

# if __name__ == "__main__":
#     main()


def parse_map(input_text):
    return [list(line) for line in input_text.strip().splitlines()]

def get_start_position(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '^':
                return (x, y)
    return None

def is_valid_position(pos, grid):
    x, y = pos
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def get_next_position(pos, direction):
    x, y = pos
    dx, dy = direction
    return (x + dx, y + dy)

def simulate_patrol(grid, obstacle_pos=None):
    grid = [row[:] for row in grid]  # Make copy
    start_pos = get_start_position(grid)
    if obstacle_pos and obstacle_pos == start_pos:
        return None
    
    if obstacle_pos:
        x, y = obstacle_pos
        grid[y][x] = '#'
    
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
    current_dir = 0
    pos = start_pos
    path = []
    visited_states = set()  # (position, direction) pairs
    
    while True:
        state = (pos, current_dir)
        if state in visited_states:
            return path  # Found a loop
        visited_states.add(state)
        path.append(pos)
        
        next_pos = get_next_position(pos, directions[current_dir])
        if not is_valid_position(next_pos, grid):
            return None  # Exits map
            
        x, y = next_pos
        if grid[y][x] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            pos = next_pos

def solve_part2(input_text):
    grid = parse_map(input_text)
    valid_positions = 0
    unique_loops = set()  # Track unique loops
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.':  # Try placing obstacle at empty positions
                path = simulate_patrol(grid, (x, y))
                if path:
                    loop = tuple(sorted(path))  # Normalize loop representation
                    if loop not in unique_loops:
                        unique_loops.add(loop)
                        valid_positions += 1
    
    return valid_positions

def main():
    with open('input.txt', 'r') as file:
        input_text = file.read()
    
    result1 = solve_part1(input_text)
    print(f"Part 1: Guard visits {result1} distinct positions")
    
    result2 = solve_part2(input_text)
    print(f"Part 2: {result2} possible obstacle positions")

if __name__ == "__main__":
    main()