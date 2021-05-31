import re

file = open("Input.txt", "r")
lines = file.readlines()

bots = {}
outputs = {}
instructions = []
chips_to_compare = [17, 61]
who_compared = 0
compared = False

for line in lines:
    results = re.findall(r"\w+", line)
    if results[0] == 'value':
        value = int(results[1])
        bot = results[5]
        if bot in bots:
            bots[bot].append(value)
        else:
            bots.update({bot: [value]})
    elif results[0] == 'bot':
        tmp = [results[1]]
        if results[5] == 'bot':
            tmp.append('bot')
        else:
            tmp.append('output')
        tmp.append(results[6])
        if results[10] == 'bot':
            tmp.append('bot')
        else:
            tmp.append('output')
        tmp.append(results[11])
        instructions.append(tmp)
    while True:
        toDo = False
        for instruction in instructions:
            for bot in dict(bots):
                if len(bots[bot]) == 2 and bot == instruction[0]:
                    toDo = True
                    bots[bot].sort()
                    if (bots[bot][0] == chips_to_compare[0] and bots[bot][1] == chips_to_compare[1] and not compared):
                        who_compared = bot
                        compared = True
                    if instruction[1] == 'bot':
                        if instruction[2] in bots:
                            bots[instruction[2]].append(bots[bot][0])
                            if instruction[3] == 'bot':
                                if instruction[4] in bots:
                                    bots[instruction[4]].append(bots[bot][1])
                                else:
                                    bots.update({instruction[4]: [bots[bot][1]]})
                            elif instruction[3] == 'output':
                                if instruction[4] in outputs:
                                    outputs[instruction[4]].append(bots[bot][1])
                                else:
                                    outputs.update({instruction[4]: [bots[bot][1]]})
                        else:
                            bots.update({instruction[2]: [bots[bot][0]]})
                            if instruction[3] == 'bot':
                                if instruction[4] in bots:
                                    bots[instruction[4]].append(bots[bot][1])
                                else:
                                    bots.update({instruction[4]: [bots[bot][1]]})
                            elif instruction[3] == 'output':
                                if instruction[4] in outputs:
                                    outputs[instruction[4]].append(bots[bot][1])
                                else:
                                    outputs.update({instruction[4]: [bots[bot][1]]})
                            
                    elif instruction[1] == 'output':
                        if instruction[2] in outputs:
                            outputs[instruction[2]].append(bots[bot][0])
                            if instruction[3] == 'bot':
                                if instruction[4] in bots:
                                    bots[instruction[4]].append(bots[bot][1])
                                else:
                                    bots.update({instruction[4]: [bots[bot][1]]})
                            elif instruction[3] == 'output':
                                if instruction[4] in outputs:
                                    outputs[instruction[4]].append(bots[bot][1])
                                else:
                                    outputs.update({instruction[4]: [bots[bot][1]]})
                        else:
                            outputs.update({instruction[2]: [bots[bot][0]]})
                            if instruction[3] == 'bot':
                                if instruction[4] in bots:
                                    bots[instruction[4]].append(bots[bot][1])
                                else:
                                    bots.update({instruction[4]: [bots[bot][1]]})
                            elif instruction[3] == 'output':
                                if instruction[4] in outputs:
                                    outputs[instruction[4]].append(bots[bot][1])
                                else:
                                    outputs.update({instruction[4]: [bots[bot][1]]})
                    bots[bot] = []
        if not toDo:
            break

print("Bots:")
print(bots)
print("Outputs:")
print(outputs)
print("Instructions:")
print(instructions)
print("Who compared:")
print(who_compared)
print(outputs['0'][0] * outputs['1'][0] * outputs['2'][0])