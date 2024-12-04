import re


def partone(puzzleinput):
    games = puzzleinput.split('\n')
    possible_games = []
    total = 0
    #only 12 red, 13 green, 14 blue
    for game in games:
        game_impossible = False
        split_by_colon = game.split(':')
        after_colon = split_by_colon[1].strip()
        split_by_semicolon = after_colon.split(';')
        split_by_semicolon = [item.strip() for item in split_by_semicolon]
        #print(split_by_colon[0])
        for item in split_by_semicolon:
            cubes = item.split(',')
            for cube in cubes:
                count, color = cube.strip().split(' ')
                count = int(count)

                if (color == 'red' and count > 12) or (color == 'green' and count > 13) or (color =='blue' and count > 14):
                    game_impossible = True
                    break
                #else:
                    #print(split_by_colon[0], "possible")
            if game_impossible:
                break
        if not game_impossible:
            possible_games.append(game)
    for possiblegame in possible_games:
        game = possiblegame.split(':')
        #print(game[0])
        gamenumber = re.findall('\d+', game[0])
        #print(int(gamenumber[0]))
        total += int(gamenumber[0])

    print(total)
    #print(possible_games)


def parttwo(puzzleinput):

    puzzle_dict = {}
    games = puzzleinput.split('\n')
    for game in games:
        gameFirstSplit = game.split(':')
        gameNum = gameFirstSplit[0]
        # print(gameNum)
        gameContents = gameFirstSplit[1].split(';')
        # print(gameContents)
        puzzle_dict.update({gameNum: gameContents})
    #print(puzzle_dict)
    Games_Dict = {}

    for key in puzzle_dict:
        # print(key, '->', puzzle_dict[key])
        gameRound_dict = {'red': 0, 'green': 0, 'blue': 0}
        for gameRound in puzzle_dict[key]:

            #print(key, '->', gameRound)
            cubes = gameRound.split(',')
            for cube in cubes:
                count, color = cube.strip().split(' ')
                count = int(count)
                #print(color, count, ' testing ', gameRound_dict.get(color))
                if count > int(gameRound_dict[color]):
                    update = {color: count}
                    gameRound_dict.update(update)
            #print(gameRound_dict)
        Games_Dict.update({key: gameRound_dict})
    GamesTotals = []
    for game in Games_Dict.items():
        gameTotal = 0
        #print(Games_Dict[game[0]])
        #print(game[0])
        red = int(Games_Dict[game[0]].get('red'))
        #print(red)
        green = int(Games_Dict[game[0]].get('green'))
        #print(green)
        blue = int(Games_Dict[game[0]].get('blue'))
        #print(blue)
        total = red * green * blue
        GamesTotals.append(total)
    print(sum(GamesTotals))

def main():

    puzzleinput = open('input.txt', 'r').read()
    partone(puzzleinput)
    parttwo(puzzleinput)


if __name__ == "__main__":
    main()
