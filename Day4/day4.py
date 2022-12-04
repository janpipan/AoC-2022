def fullContains(range1, range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return True
    if range2[0] >= range1[0] and range2[1] <= range1[1]:
        return True
    return False

def overlaps(range1, range2):
    if range1[0] >= range2[0] and range1[0] <= range2[1]:
        return True
    if range1[1] >= range2[0] and range1[1] <= range2[1]:
        return True
    if range2[0] >= range1[0] and range2[0] <= range1[1]:
        return True
    if range2[1] >= range1[0] and range2[1] <= range1[1]:
        return True
    return False

if __name__ == '__main__':
    sum = 0
    sumOverlaps = 0
    with open('day4.txt') as file:
        for line in file:
            line = line.strip().split(",")
            range1, range2 = line[0].split("-"), line[1].split("-")
            range1, range2 = [int(x) for x in range1], [int(x) for x in range2]
            if fullContains(range1, range2):
                sum += 1
            if overlaps(range1, range2):
                sumOverlaps += 1

    print(sum)
    print(sumOverlaps)