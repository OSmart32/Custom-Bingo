import json
import random
import pyperclip # pip install pyperclip


with open('extinction_bingo_goals.json', 'r') as goalsFile:
    goalList = json.load(goalsFile) # load json into list of dictionaries (key, value)



def getStage(): # return the user's option
    stage = 0
    while stage == 0:
        try:
            stage = int(input('What stage do you want to go up to? 1-3, goes up to midgame: '))
        except ValueError:
            print('You did not enter a valid stage!')
    return stage



stage = getStage()
goalList = list(filter(lambda x: x['stage'] <= stage, goalList)) # filter out the goals where the stage is higher than what the user wants

count = 0
goalNames = []

while count < 25:
    
    goal = random.choice(goalList)
    goalNames.append(goal['name'])
    
    if goal.__contains__('group'):
        if goal['group'] == 'Craft':
            tierCrafts = list(filter(lambda x: ((x.__contains__('group')) and (x['group'] == goal['group']) and (x['stage'] == goal['stage'])), goalList))
            for g in tierCrafts:
                goalList.remove(g)
        else:
            goalList = list(filter(lambda x: (not x.__contains__('group')) or (x['group'] != goal['group']), goalList))
    else:
        goalList.remove(goal)
    
    count += 1


outGoals = [] # store the json file as a list of strings
outGoals.append('[')

for i in range(0, 25): # remove the comma from the last goal since bingosync does not like that
    if i < 24:
        outGoals.append('{"name": ' + f'"{goalNames[i]}"' + "},")
    else:
        outGoals.append('{"name": ' + f'"{goalNames[i]}"' + "}")

outGoals.append(']')

pyperclip.copy('\n'.join(outGoals)) # copy goals directly to clipboard
