def getInput():
    data = []
    
    with open('input.txt', 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            data.append(numbers)
    return data

def is_safe(report):
    return (all(x < y for x, y in zip(report, report[1:])) or all(x > y for x, y in zip(report, report[1:]))) and \
           all(1 <= abs(x - y) <= 3 for x, y in zip(report, report[1:]))

def check_reports(data):
    safe_reports = 0
    
    for report in data:
        if is_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i+1:]
                if is_safe(modified_report):
                    safe_reports += 1
                    break
    
    return safe_reports

data = getInput()
safe_reports = check_reports(data)
print(safe_reports)
