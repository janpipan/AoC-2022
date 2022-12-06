

if __name__ == '__main__':
    text = ''
    start = 0   
    start2 = 0 
    with open('day6.txt') as file:
        for line in file:
            text = line

    for i in range(len(text)-4):
        letters = set(text[i:i+4])
        if len(letters) == 4:
            start = i + 4
            for j in range(start, len(text)-14):
                lettersMsg = set(text[j:j+14])
                if len(lettersMsg) == 14:
                    start2 = j + 14
                    break
            break

    print(start)
    print(start2)


