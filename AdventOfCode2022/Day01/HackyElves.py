elves = open('AdventDay1Example.txt', 'r').read().split('\n')
print(elves)

IntList = []
for elf in elves:
    result = int(elf.strip() or 0)
    IntList.append(result)
    
print(IntList)
    
listToStr = ' '.join(map(str, IntList))
print(listToStr)
StrToList = listToStr.split(' 0 ')
print(StrToList)
totals = []
for num in StrToList:
    totals.append(sum(int(char) for char in num.split(' ') if char.isdigit()))
    print(totals)
    
print (max(totals))
