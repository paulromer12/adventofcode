def evaluate(nums, ops):
    """Evaluate expression left-to-right with given numbers and operators"""
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i + 1]
        elif ops[i] == '*':
            result *= nums[i + 1]
        else:  # '||'
            # Convert both numbers to strings, concatenate, then back to int
            result = int(str(result) + str(nums[i + 1]))
    return result

def find_valid_combinations(test_value, nums):
    """Try all possible operator combinations"""
    if len(nums) == 1:
        return nums[0] == test_value
        
    ops = ['+', '*', '||']
    num_ops = len(nums) - 1
    
    # Try all possible combinations of operators
    for i in range(3 ** num_ops):  # 3 operators, num_ops positions
        current_ops = []
        n = i
        for _ in range(num_ops):
            current_ops.append(ops[n % 3])
            n //= 3
                
        try:
            if evaluate(nums, current_ops) == test_value:
                return True
        except:
            # Skip invalid combinations (e.g., numbers too large)
            continue
    
    return False

def solve_calibration():
    total = 0
    
    with open('input.txt') as f:
        for line in f:
            # Parse each line
            parts = line.strip().split(':')
            test_value = int(parts[0])
            nums = [int(x) for x in parts[1].strip().split()]
            
            # Check if equation can be solved
            if find_valid_combinations(test_value, nums):
                total += test_value
                
    return total

if __name__ == "__main__":
    result = solve_calibration()
    print(f"Total calibration result: {result}")