import copy

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

    return True

def conditions(generators, chips, floorNumber):
     canBringTwoUp = False
     canBringOneDown = False

     gmCombinations = []

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
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                canBringTwoUp = True
        elif floorNumber == 3:
            generatorsCopy[floorNumber - 1].append(g)
            chipsCopy[floorNumber - 1].append(m)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                pass
        else:
            generatorsCopy[floorNumber + 1].append(g)
            chipsCopy[floorNumber + 1].append(m)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                canBringTwoUp = True
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
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                pass

     generatorsCopy = copy.deepcopy(generators)
     chipsCopy = copy.deepcopy(chips)
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
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                    canBringTwoUp = True
            elif floorNumber == 3:
                generatorsCopy[floorNumber - 1].append(g1)
                generatorsCopy[floorNumber - 1].append(g2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                    pass
            else:
                generatorsCopy[floorNumber + 1].append(g1)
                generatorsCopy[floorNumber + 1].append(g2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                    canBringTwoUp = True
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
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                    pass

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
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                    canBringTwoUp = True
            elif floorNumber == 3:
                chipsCopy[floorNumber - 1].append(m1)
                chipsCopy[floorNumber - 1].append(m2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                    pass
            else:
                chipsCopy[floorNumber + 1].append(m1)
                chipsCopy[floorNumber + 1].append(m2)
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                    canBringTwoUp = True
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
                if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                    pass

     generatorsCopy = copy.deepcopy(generators)
     chipsCopy = copy.deepcopy(chips)
     elevatorGenerators = []
     elevatorChips = []
    
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
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                pass
        elif floorNumber == 3:
            generatorsCopy[floorNumber - 1].append(g)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips)  and [generatorsCopy, chipsCopy, floorNumber - 1]:
                canBringOneDown = True
        else:
            generatorsCopy[floorNumber + 1].append(g)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips)  and [generatorsCopy, chipsCopy, floorNumber + 1]:
                pass
            generatorsCopy = copy.deepcopy(generators)
            chipsCopy = copy.deepcopy(chips)
            elevatorGenerators = []
            elevatorChips = []
            g = generatorsCopy[floorNumber].pop(i)
            elevatorGenerators.append(g)
            generatorsCopy[floorNumber - 1].append(g)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips)  and [generatorsCopy, chipsCopy, floorNumber - 1]:
                canBringOneDown = True

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
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                pass
        elif floorNumber == 3:
            chipsCopy[floorNumber - 1].append(g)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                canBringOneDown = True
        else:
            chipsCopy[floorNumber + 1].append(g)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber + 1]:
                pass
            generatorsCopy = copy.deepcopy(generators)
            chipsCopy = copy.deepcopy(chips)
            elevatorGenerators = []
            elevatorChips = []
            g = chipsCopy[floorNumber].pop(i)
            elevatorChips.append(g)
            chipsCopy[floorNumber - 1].append(g)
            if isValid(generatorsCopy, chipsCopy, elevatorGenerators, elevatorChips) and [generatorsCopy, chipsCopy, floorNumber - 1]:
                canBringOneDown = True

    #  print(canBringTwoUp)
    #  print(canBringOneDown)
     return canBringTwoUp, canBringOneDown