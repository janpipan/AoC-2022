if __name__ == '__main__':
    grid = []
    with open('test.txt') as file:
        for line in file:
            line = line.strip()
            row = []
            for digit in range(len(line)):
                row.append(int(line[digit]))
            grid.append(row)
    right = len(grid[0])
    down = len(grid)
    sum = right * 4 - 4
    max = 4
    for row in range(1,down - 1):
        for col in range(1,right - 1):
            height = grid[row][col]
            # left
            index = 1
            visible = False
            treeHouse = 1
            treeHouseIndex = 1
            while col - index >= 0:
                if grid[row][col-index] >= height:
                    treeHouseIndex += 1
                    break
                index += 1
                treeHouseIndex += 1
            treeHouse *= treeHouseIndex - 1
            if col - index == -1 and not visible:
                sum += 1
                visible = True
            # right
            index = 1
            treeHouseIndex = 1
            while col + index < right:
                if grid[row][col+index] >= height:
                    treeHouseIndex += 1
                    break
                index += 1
                treeHouseIndex += 1
            treeHouse *= treeHouseIndex - 1
            if col + index == right and not visible:
                sum += 1
                visible = True
            # up 
            index = 1
            treeHouseIndex = 1
            while row - index >= 0:
                if grid[row-index][col] >= height:
                    treeHouseIndex += 1
                    break
                index += 1
                treeHouseIndex += 1
            treeHouse *= treeHouseIndex - 1
            if row - index == -1 and not visible:
                sum += 1
                visible = True
            # down
            index = 1
            treeHouseIndex = 1
            while row + index < down:
                if grid[row+index][col] >= height:
                    treeHouseIndex += 1
                    break
                index += 1
                treeHouseIndex += 1
            treeHouse *= treeHouseIndex - 1
            if row + index == down and not visible:
                sum += 1
                visible = True
            if treeHouse > max:
                max = treeHouse
            
    print(sum)
    print(max)

