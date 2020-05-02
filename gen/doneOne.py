import json
import random
import sys

'''
Record question as done in DONE_FILE so that it won't be picked next time
'''

DONE_FILE="doneQuestions.out"

with open(DONE_FILE) as json_file:
    data = json.load(json_file)
    #print(data)
    if (len(sys.argv) > 1):
        num = int(sys.argv[1])
    #print(data)
        print("Would you like to add ", sys.argv[1], " to done list?")
        ans = input("y/n?")
        if (ans == "y" and num not in data):
            with open(DONE_FILE, 'w') as json_file:
                data.append(num)
                json.dump(data, json_file)
