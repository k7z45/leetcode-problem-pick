import json
import sys
import random

'''
Pick one leetcode problem randomly from FILE that is not in DONE_FILE
Can also specify difficulty level from command line argument by passing in 1, 2 or 3
'''

FILE="allQuestions.out"
DONE_FILE="doneQuestions.out"
with open(DONE_FILE) as json_file:
    done = json.load(json_file)

with open(FILE) as json_file:
    data = json.load(json_file)
    #print(data)
    #print(done)
    not_done = []
    for item in data:
        if (item["id"] not in done):
            not_done.append(item)
    filtered_data = []
    level = None
    if (len(sys.argv) > 1):
        level = int(sys.argv[1])

    for item in not_done:
        if (not level or item["difficulty"] == level):
            filtered_data.append(item)


    #pick = random.choice(data)
    pick = random.choice(filtered_data)
    print(pick)

