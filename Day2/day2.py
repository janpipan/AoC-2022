# part one

pick1Dict = {'A':'Rock','B':'Paper','C':'Scissors'}
pick2Dict = {'X':'Rock','Y':'Paper','Z':'Scissors'}
oppositeLoseDict = {'Rock':'Scissors','Paper':'Rock','Scissors':'Paper'}
oppositeWinDict = {'Scissors':'Rock','Rock':'Paper','Paper':'Scissors'}
weight = {'Rock':1,'Paper':2,'Scissors':3}

sum = 0
sum2 = 0
plays = []

with open("day2.txt") as file:
    for line in file:
        plays = line.strip().split(" ")
        pick1,pick2 = plays[0], plays[1]
        if pick1Dict[pick1] == 'Rock' and pick2Dict[pick2] == 'Paper':
            sum += weight[pick2Dict[pick2]] + 6
        elif pick1Dict[pick1] == 'Paper' and pick2Dict[pick2] == 'Scissors':
            sum += weight[pick2Dict[pick2]] + 6
        elif pick1Dict[pick1] == 'Scissors' and pick2Dict[pick2] == 'Rock':
            sum += weight[pick2Dict[pick2]] + 6
        elif pick1Dict[pick1] == pick2Dict[pick2]:
            sum += weight[pick2Dict[pick2]] + 3
        else:
            sum += weight[pick2Dict[pick2]]
        
        if pick2 == 'X':
            sum2 += weight[oppositeLoseDict[pick1Dict[pick1]]]
        elif pick2 == 'Y':
            sum2 += weight[pick1Dict[pick1]] + 3
        else:
            sum2 += weight[oppositeWinDict[pick1Dict[pick1]]] + 6

print(sum)

# part two

print(sum2)

