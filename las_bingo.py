import json
import random
import pyperclip # pip install pyperclip


with open('las_bingo_goals.json', 'r') as goalsFile:
    totalGoals = json.load(goalsFile) # load json into list of dictionaries (key, value)

count = 0 # keep track of how many goals we have
bingo_goals = [] # store the goal names

while count < 25: # while statement to pull 25 goals
    
    goal = random.choice(totalGoals) # get a random goal from list
    bingo_goals.append(goal['name']) # add the name value to the bingo_goals list
    
    if goal.__contains__('group'): # if goal has a 'group' key
        group = goal['group'] # store the group value
        totalGoals = list(filter(lambda x: (not x.__contains__('group')) or (x['group'] != group), totalGoals)) # create a new list of goals that either does not have a 'group' key or where the group value is not the one we just got
    else:
        totalGoals.remove(goal) # if it does not have a 'group' key just remove this specific goal
    
    count += 1 # update tracker


outGoals = [] # store the json file as a list of strings
outGoals.append('[')

for i in range(0, 25): # remove the comma from the last goal since bingosync does not like that
    if i < 24:
        outGoals.append('{"name": ' + f'"{bingo_goals[i]}"' + "},")
    else:
        outGoals.append('{"name": ' + f'"{bingo_goals[i]}"' + "}")

outGoals.append(']')


pyperclip.copy('\n'.join(outGoals)) # copy goals directly to clipboard
