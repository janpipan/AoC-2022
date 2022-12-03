
def crossSection(listA, listB):
    retList = (value for value in listA if value in listB)
    return retList

def getPriority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

def getBadge(iList):
    tempCross = crossSection(iList[0], iList[1])
    badge = crossSection(tempCross, iList[2])
    return list(set(badge))[0]



if __name__ == '__main__':
    sum = 0
    badgesSum = 0
    rucksackCounter = 0
    groupList = []

    with open("day3.txt") as file:
        for line in file:
            line = line.strip()
            if rucksackCounter < 3:
                rucksackCounter += 1
                groupList.append(list(line))
            if rucksackCounter == 3:
                rucksackCounter = 0
                badgesSum += getPriority(getBadge(groupList))
                groupList = []
            firstCompartment = list(line[:int(len(line)/2)])
            secondCompartment = list(line[-int(len(line)/2):])
            item = set(crossSection(firstCompartment, secondCompartment))
            if len(item) < 1:
                continue
            item = list(item)[0]
            sum += getPriority(item)

    
    print(sum)
    print(badgesSum)