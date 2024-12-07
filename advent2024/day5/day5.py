# from collections import defaultdict, deque

# def is_valid_order(pages, rules):
#     # Create adjacency list and in-degree count
#     graph = defaultdict(list)
#     in_degree = defaultdict(int)
    
#     # Only consider rules involving pages in this update
#     relevant_rules = [
#         (x, y) for x, y in rules 
#         if x in pages and y in pages
#     ]
    
#     # Build graph and in-degree
#     for x, y in relevant_rules:
#         # Check if the rule is violated in current update
#         x_index = pages.index(x)
#         y_index = pages.index(y)
#         if x_index > y_index:
#             return False
        
#         graph[x].append(y)
#         in_degree[y] += 1
    
#     # Initialize queue with pages having zero in-degree
#     queue = deque([p for p in pages if in_degree[p] == 0])
#     sorted_order = []
    
#     # Topological sort
#     while queue:
#         current = queue.popleft()
#         sorted_order.append(current)
        
#         for neighbor in graph[current]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
    
#     # Check if full topological sort is possible
#     valid = len(sorted_order) == len(set(pages))
    
#     # Debugging print for both valid and invalid updates
#     if not valid:
#         print(f"Invalid update: {pages}")
#         print(f"Relevant rules: {relevant_rules}")
#         print(f"Sorted order: {sorted_order}")
#     else:
#         print(f"Valid update: {pages}")
#         print(f"Relevant rules: {relevant_rules}")
#         print(f"Sorted order: {sorted_order}")
    
#     return valid

# def solve_page_ordering(filename):
#     # Read input from file
#     with open(filename, 'r') as file:
#         lines = file.read().strip().split('\n')
    
#     # Find the first empty line or end of rules
#     try:
#         split_index = next(i for i, line in enumerate(lines) if not line.strip())
#     except StopIteration:
#         # If no empty line, assume all lines are rules
#         split_index = len(lines)
    
#     # Parse rules
#     rules = [tuple(map(int, line.split('|'))) for line in lines[:split_index] if line.strip()]
    
#     # Parse updates
#     updates = [list(map(int, update.split(','))) for update in lines[split_index+1:] if update.strip()]
    
#     # Find valid updates and their middle pages
#     valid_middle_pages = []
    
#     for update in updates:
#         if is_valid_order(update, rules):
#             middle_index = len(update) // 2
#             valid_middle_pages.append(update[middle_index])
    
#     return sum(valid_middle_pages)

# # Solve the puzzle
# if __name__ == "__main__":
#     solution = solve_page_ordering('input.txt')
#     print("Final solution:", solution)

from collections import defaultdict, deque

def reorder_pages(pages, rules):
    # Create adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Only consider rules involving pages in this update
    relevant_rules = [
        (x, y) for x, y in rules 
        if x in pages and y in pages
    ]
    
    # Build graph and in-degree
    for x, y in relevant_rules:
        graph[x].append(y)
        in_degree[y] += 1
    
    # Initialize queue with pages having zero in-degree
    queue = deque([p for p in pages if in_degree[p] == 0])
    sorted_order = []
    
    # Topological sort
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if full topological sort is possible
    if len(sorted_order) == len(set(pages)):
        # Reorder pages based on topological sort
        return sorted_order
    
    # If no valid order found, return original pages
    return pages

def solve_page_ordering(filename):
    # Read input from file
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
    
    # Find the first empty line or end of rules
    try:
        split_index = next(i for i, line in enumerate(lines) if not line.strip())
    except StopIteration:
        # If no empty line, assume all lines are rules
        split_index = len(lines)
    
    # Parse rules
    rules = [tuple(map(int, line.split('|'))) for line in lines[:split_index] if line.strip()]
    
    # Parse updates
    updates = [list(map(int, update.split(','))) for update in lines[split_index+1:] if update.strip()]
    
    # Find middle pages of reordered updates
    valid_middle_pages = []
    
    for update in updates:
        # Attempt to reorder pages
        reordered = reorder_pages(update, rules)
        
        # Check if reordering actually changed the update
        if reordered != update:
            middle_index = len(reordered) // 2
            valid_middle_pages.append(reordered[middle_index])
    
    return sum(valid_middle_pages)

# Solve the puzzle
if __name__ == "__main__":
    solution = solve_page_ordering('input.txt')
    print("Final solution:", solution)