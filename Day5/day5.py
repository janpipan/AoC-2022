if __name__ == '__main__':
    n = 0
    crateList = []
    with open('day5.txt') as file:
        for line in file:
            if line.strip()[0] == '1':
                n = int(line.strip()[-1])
                break
        crateList = [[] for _ in range(n)]
    with open('day5.txt') as file:
        for line in file:
            if line == '\n':
                break
            counter = 0
            for char in line:
                if char == '[':
                    crateList[int(counter/4)].append(line[counter+1])
                counter+=1
    crateList2 = []
    for item in crateList:
        item.reverse()
        crateList2.append(item.copy())
    with open('day5.txt') as file:
        for line in file:
            line = line.strip().split(" ")
            if line[0] == 'move':
                for i in range(int(line[1])):
                    crate = crateList[int(line[3])-1].pop()
                    crateList[int(line[5])-1].append(crate)
    topCrates = ""
    for item in crateList:
        topCrates += item[-1]
    print(topCrates)
    # task 2
    with open('day5.txt') as file:
        for line in file:
            line = line.strip().split(" ")
            if line[0] == 'move':
                crates = crateList2[int(line[3])-1][-int(line[1]):]
                for i in range(int(line[1])):
                    crate = crateList2[int(line[3])-1].pop()
                for crate in crates:
                    crateList2[int(line[5])-1].append(crate)

    topCrates2 = ""
    for item in crateList2:
        topCrates2 += item[-1]

    print(topCrates2)
