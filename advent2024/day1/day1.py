def getInput():
    list1 = []
    list2 = []
    
    with open('input.txt', 'r') as file:
        for line in file:
            numbers = line.split()
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))
    return list1, list2

def sortListSmallestLargest(lst):
    return sorted(lst)

def calculateSimilarityScore(list1, list2):
    score = 0
    for num in list1:
        score += num * list2.count(num)
    return score

def diffLists(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(abs(list1[i] - list2[i]))
    return list3

list1, list2 = getInput()
list1 = sortListSmallestLargest(list1)
list2 = sortListSmallestLargest(list2)

list3 = diffLists(list1, list2)
totalSum = sum(list3)
similarityScore = calculateSimilarityScore(list1, list2)

print(totalSum)
print(similarityScore)