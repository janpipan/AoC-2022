# part one
calorieList = []

with open("day1.txt") as file:
    calorieCount = 0
    for line in file:
        if line != '\n':
            calorieCount += int(line)
        else:
            calorieList.append(calorieCount)
            calorieCount = 0


print(max(calorieList))

# part two

calorieList.sort(reverse=True)

print(sum(calorieList[:3]))
