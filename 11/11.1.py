import re

floors = [['PoG', 'TG', 'TM', 'PrG', 'RG', 'RM', 'CG', 'CM'], 
          ['PoM', 'PrM'], 
          [], 
          []]

elevator_floor = 1

steps = 0

up = True

for floor in floors:
    print(floor)


while True:
    if elevator_floor != 1:
        print()

    if up:
        selected_items = []
        floorA = []
        typesA = []
        floorB = []
        typesB = []

        for element in floors[elevator_floor - 1]:
            floorA.append(element.split('G', 1)[0].split('M', 1)[0])
            if 'G' in element:
                typesA.append('G')
            else:
                typesA.append('M')

        print(floorA)
        print(typesA)

        for element in floors[elevator_floor]:
            floorB.append(element.split('G', 1)[0].split('M', 1)[0])
            if 'G' in element:
                typesB.append('G')
            else:
                typesB.append('M')

        print(floorB)
        print(typesB)

        
    else:
        print()

    break

floors[elevator_floor].append(floors[elevator_floor - 1][0])
floors[elevator_floor].append(floors[elevator_floor - 1][3])
print("sdsd")
floors[elevator_floor - 1].pop(0)
floors[elevator_floor - 1].pop(3)
steps += 1
elevator_floor += 1

for floor in floors:
    print(floor)