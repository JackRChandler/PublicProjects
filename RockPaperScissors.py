outcomes = open('AdventDay2Input.txt', 'r').read().split('\n')

#for match in outcomes:
    

def assignValues(input):
    if input == 'A':
        return 1
    elif input == 'B':
        return 2
    elif input == 'C':
        return 3
    elif input == 'X':
        return 1
    elif input == 'Y':
        return 2
    elif input == 'Z':
        return 3

final = []
for match in outcomes:
    totals = []
    for letter in match.split(' '):
#        print(letter)
        totals.append(assignValues(letter))
#        print(totals)
#        print("inside letter loop")
#    print(sum(totals))
    MatchScore = []
    if totals == [1,1]:
        MatchScore.append(4)
    elif totals == [1,2]:
        MatchScore.append(8)
    elif totals == [1,3]:
        MatchScore.append(3)
    elif totals == [2,1]:
        MatchScore.append(1)
    elif totals == [2,2]:
        MatchScore.append(5)
    elif totals == [2,3]:
        MatchScore.append(9)
    elif totals == [3,1]:
        MatchScore.append(7)
    elif totals == [3,2]:
        MatchScore.append(2)
    elif totals == [3,3]:
        MatchScore.append(6)
#    print(totals)
#    print(sum(totals))  
#    print(MatchScore)
    final.extend(MatchScore)
#    print("inside match loop")
#print(final)
print("Final score is:", sum(final))  

#print(outcomes)

#### For part 2
outcomes = open('AdventDay2Input.txt', 'r').read().split('\n')

#for match in outcomes:
    

def assignValues(input):
    if input == 'A':
        return 1
    elif input == 'B':
        return 2
    elif input == 'C':
        return 3
    elif input == 'X':
        return 1
    elif input == 'Y':
        return 2
    elif input == 'Z':
        return 3

final = []
for match in outcomes:
    totals = []
    for letter in match.split(' '):
#        print(letter)
        totals.append(assignValues(letter))
#        print(totals)
#        print("inside letter loop")
#    print(sum(totals))
    MatchScore = []
    if totals == [1,1]: # I lose and I play scissors
        MatchScore.append(3)
    elif totals == [1,2]: # I draw and I play rock
        MatchScore.append(4)
    elif totals == [1,3]: # I win and I play paper
        MatchScore.append(8)
    elif totals == [2,1]: # I lose and I play rock
        MatchScore.append(1)
    elif totals == [2,2]: # I draw and I play paper
        MatchScore.append(5)
    elif totals == [2,3]: # I win and I play scissors
        MatchScore.append(9)
    elif totals == [3,1]: # I lose and I play paper
        MatchScore.append(2)
    elif totals == [3,2]: # I draw and I play scissors
        MatchScore.append(6)
    elif totals == [3,3]: # I win and I play rock
        MatchScore.append(7)
#    print(totals)
#    print(sum(totals))  
#    print(MatchScore)
    final.extend(MatchScore)
#    print("inside match loop")
#print(final)
print("Final score is:", sum(final))  

#print(outcomes)
