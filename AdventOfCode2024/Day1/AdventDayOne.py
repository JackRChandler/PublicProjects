

def partone(puzzleinput):
    listone = []
    listtwo = []
    lines = puzzleinput.split('\n')
    for line in lines:
        number = line.split()
        # print(number)
        listone.append(number[0])
        listtwo.append(number[1])
    listone.sort()
    listtwo.sort()
    # print(listone)
    # print(listtwo)
    distance = [max(int(a), int(b)) - min(int(a), int(b)) for a, b in zip(listone, listtwo)]
    print(sum(distance))

def parttwo(puzzleinput):
    listone = []
    listtwo = []
    lines = puzzleinput.split('\n')
    for line in lines:
        number = line.split()
        listone.append(number[0])
        listtwo.append(number[1])
    listone.sort()
    listtwo.sort()
    # print(listone)
    # print(listtwo)
    similaritylist = []
    for numberone in listone:
        combinelist = []
        numberfound = 0
        for numbertwo in listtwo:
            if numberone == numbertwo:
                #print(numberone)
                numberfound += 1
                # print(numberfound)
        similarityscore = int(numberone) * int(numberfound)
        # print(similarityscore)
        combinelist.append(similarityscore)
        combinelist.append(numberone)
        similaritylist.append(combinelist)
    # print(similaritylist)
    total = sum(score[0] for score in similaritylist)
    print(total)

def main():
    puzzleinput = open('input.txt', 'r').read()
    partone(puzzleinput)
    parttwo(puzzleinput)


if __name__ == "__main__":
    main()
