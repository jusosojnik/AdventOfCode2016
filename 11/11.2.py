import copy
import conditions

generators = [['AG', 'BG', 'CG', 'DG', 'EG'], 
              [], 
              [], 
              []]

chips = [['BM', 'DM', 'EM'], 
         ['AM', 'CM'], 
         [], 
         []]

floorNumber = 0;
processedMoves = [[generators, chips, floorNumber]]

def isValid(generators, chips, elevatorGenerators, elevatorChips):
    if len(elevatorChips) != 0:
        for generator in elevatorGenerators:
            for chip in elevatorChips:
                if generator[0] != chip[0]:
                    return False

    for i, floor in enumerate(chips):
        if len(generators[i]) != 0:
            for chip in floor:
                check = False
                for generator in generators[i]:
                    if generator[0] == chip[0]:
                        check = True
                        break
                if not check:
                    return False
    emp = 0
    for i in range(len(chips) - 1):
        if len(chips[i]) == 0 and len(generators[i]) == 0:
            emp += 1

    k = 0
    for i in range(len(chips)):
        k += len(chips[i]) + len(generators[i])

    if emp == 3:
        raise Exception((generators, chips, floorNumber))
    
    if k != 10:
        print("Count Error")
        raise Exception((generators, chips, floorNumber))

    return True

def makeValidMoves(generators, chips, floorNumber):
     validMoves = []
     gmCombinations = []
     interchangable = False
     canBringTwoUp, canBringOneDown = conditions.conditions(generators, chips, floorNumber)
    #  print(canBringTwoUp, canBringOneDown)

     # G + C
     for i, generator in enumerate(generators[floorNumber]):
        for j, chip in enumerate(chips[floorNumber]):
            if generator[0] == chip[0]:
                gmCombinations.append([i, j])
                break;

     generatorsCopy = copy.deepcopy(generators)
     chipsCopy = copy.deepcopy(chips)
     elevatorGenerators = []
     elevatorChips = []

     for combination in gmCombinations:
        generatorsCopy = copy.deepcopy(generators)
        chipsCopy = copy.deepcopy(chips)
        elevatorGenerators = []
        elevatorChips = []
        g = generatorsCopy[floorNumber].pop(combination[0])
        m = chipsCopy[floorNumber].pop(combination[1])
        elevatorGenerators.append(g)
        elevatorChips.append(m)

        if floorNumber == 0:
            generatorsCopy[floorNumber + 1].append(g)
            chipsCopy[floorNumber + 1].append(m)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
        elif floorNumber == 3:
            generatorsCopy[floorNumber - 1].append(g)
            chipsCopy[floorNumber - 1].append(m)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves and not canBringOneDown:
                validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
        else:
            generatorsCopy[floorNumber + 1].append(g)
            chipsCopy[floorNumber + 1].append(m)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
            generatorsCopy = copy.deepcopy(generators)
            chipsCopy = copy.deepcopy(chips)
            elevatorGenerators = []
            elevatorChips = []
            g = generatorsCopy[floorNumber].pop(combination[0])
            m = chipsCopy[floorNumber].pop(combination[1])
            elevatorGenerators.append(g)
            elevatorChips.append(m)
            generatorsCopy[floorNumber - 1].append(g)
            chipsCopy[floorNumber - 1].append(m)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves and not canBringOneDown:
                validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])

     generatorsCopy = copy.deepcopy(generators)
     chipsCopy = copy.deepcopy(chips)
     elevatorChips = []
     elevatorChips = []

     # G + G
     for i in range(len(generators[floorNumber])):
        if i == len(generators[floorNumber]) - 1:
            break
        for j in range(i + 1, len(generators[floorNumber])):
            generatorsCopy = copy.deepcopy(generators)
            chipsCopy = copy.deepcopy(chips)
            elevatorGenerators = []
            elevatorChips = []
            g1 = generatorsCopy[floorNumber].pop(i)
            g2 = generatorsCopy[floorNumber].pop(j - 1)
            elevatorGenerators.append(g1)
            elevatorGenerators.append(g2)
            if floorNumber == 0:
                generatorsCopy[floorNumber + 1].append(g1)
                generatorsCopy[floorNumber + 1].append(g2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
            elif floorNumber == 3:
                generatorsCopy[floorNumber - 1].append(g1)
                generatorsCopy[floorNumber - 1].append(g2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves and not canBringOneDown:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
            else:
                generatorsCopy[floorNumber + 1].append(g1)
                generatorsCopy[floorNumber + 1].append(g2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                generatorsCopy = copy.deepcopy(generators)
                chipsCopy = copy.deepcopy(chips)
                elevatorGenerators = []
                elevatorChips = []
                g1 = generatorsCopy[floorNumber].pop(i)
                g2 = generatorsCopy[floorNumber].pop(j - 1)
                elevatorGenerators.append(g1)
                elevatorGenerators.append(g2)
                generatorsCopy[floorNumber - 1].append(g1)
                generatorsCopy[floorNumber - 1].append(g2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves and not canBringOneDown:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])

     generatorsCopy = copy.deepcopy(generators)
     chipsCopy = copy.deepcopy(chips)
     elevatorGenerators = []
     elevatorChips = []

     # C + C
     for i in range(len(chips[floorNumber])):
        if i == len(chips[floorNumber]) - 1:
            break
        for j in range(i + 1, len(chips[floorNumber])):
            generatorsCopy = copy.deepcopy(generators)
            chipsCopy = copy.deepcopy(chips)
            elevatorGenerators = []
            elevatorChips = []
            m1 = chipsCopy[floorNumber].pop(i)
            m2 = chipsCopy[floorNumber].pop(j - 1)
            elevatorChips.append(m1)
            elevatorChips.append(m2)
            if floorNumber == 0:
                chipsCopy[floorNumber + 1].append(m1)
                chipsCopy[floorNumber + 1].append(m2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
            elif floorNumber == 3:
                chipsCopy[floorNumber - 1].append(m1)
                chipsCopy[floorNumber - 1].append(m2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves and not canBringOneDown:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
            else:
                chipsCopy[floorNumber + 1].append(m1)
                chipsCopy[floorNumber + 1].append(m2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                generatorsCopy = copy.deepcopy(generators)
                chipsCopy = copy.deepcopy(chips)
                elevatorGenerators = []
                elevatorChips = []
                m1 = chipsCopy[floorNumber].pop(i)
                m2 = chipsCopy[floorNumber].pop(j - 1)
                elevatorChips.append(m1)
                elevatorChips.append(m2)
                chipsCopy[floorNumber - 1].append(m1)
                chipsCopy[floorNumber - 1].append(m2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves and not canBringOneDown:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])

     generatorsCopy = copy.deepcopy(generators)
     chipsCopy = copy.deepcopy(chips)
     elevatorGenerators = []
     elevatorChips = []
    
     if not canBringTwoUp:
        # G
        for i in range(len(generators[floorNumber])):
            generatorsCopy = copy.deepcopy(generators)
            chipsCopy = copy.deepcopy(chips)
            elevatorGenerators = []
            elevatorChips = []
            g = generatorsCopy[floorNumber].pop(i)
            elevatorGenerators.append(g)
            if floorNumber == 0:
                generatorsCopy[floorNumber + 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
            elif floorNumber == 3:
                generatorsCopy[floorNumber - 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips)  and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
            else:
                generatorsCopy[floorNumber + 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips)  and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                generatorsCopy = copy.deepcopy(generators)
                chipsCopy = copy.deepcopy(chips)
                elevatorGenerators = []
                elevatorChips = []
                g = generatorsCopy[floorNumber].pop(i)
                elevatorGenerators.append(g)
                generatorsCopy[floorNumber - 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips)  and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])

        generatorsCopy = copy.deepcopy(generators)
        chipsCopy = copy.deepcopy(chips)
        elevatorGenerators = []
        elevatorChips = []

        # C
        for i in range(len(chips[floorNumber])):
            generatorsCopy = copy.deepcopy(generators)
            chipsCopy = copy.deepcopy(chips)
            elevatorGenerators = []
            elevatorChips = []
            g = chipsCopy[floorNumber].pop(i)
            elevatorChips.append(g)
            if floorNumber == 0:
                chipsCopy[floorNumber + 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
            elif floorNumber == 3:
                chipsCopy[floorNumber - 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
            else:
                chipsCopy[floorNumber + 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber + 1])
                generatorsCopy = copy.deepcopy(generators)
                chipsCopy = copy.deepcopy(chips)
                elevatorGenerators = []
                elevatorChips = []
                g = chipsCopy[floorNumber].pop(i)
                elevatorChips.append(g)
                chipsCopy[floorNumber - 1].append(g)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1] not in processedMoves:
                    validMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])
                    processedMoves.append([generatorsCopy, chipsCopy, floorNumber - 1])

     return validMoves

# moves1 = makeValidMoves(generators, chips, floorNumber)

# print("##################")
# print(len(moves1))
# for move in moves1:
#     print(move[0])
#     print(move[1])
#     print(move[2])
#     print("")

# print(processedMoves)


def run():
    steps = 0
    moves = [[[generators, chips, floorNumber]]]
    while True:
        validMoves = []
        for move in moves[steps]:
            validMoves += makeValidMoves(move[0], move[1], move[2])
        
        moves.append(validMoves)
        steps += 1
        print(steps)
        if steps == 1:
            break

    print(len(moves))
    for i in range(len(moves)):
        for move in moves[i]:
            print(move)
            print("")


def bfs():
    steps = 0
    moves = [[[generators, chips, floorNumber]]]

    while True:
        print(steps + 1)
        validMoves = []
        for move in moves[steps]:
            validMoves += makeValidMoves(move[0], move[1], move[2])
        
        moves.append(validMoves)
        steps += 1
        if steps == 30:
            break

    print(len(moves))
    for i in range(len(moves)):
        print("############################")
        for move in moves[i]:
            print(move)
            print("")

# print(generators)
# print(chips)
# print(floorNumber)
bfs()