import requests
import pprint
import json

'''
Generate a list of leetcode algorithm ids using leetcode API and save it in FILE
'''

LEETCODE_PROBLEM_LIST="https://leetcode.com/api/problems/algorithms/"
FILE="allQuestions.out"

r = requests.get(LEETCODE_PROBLEM_LIST)
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(r.json())
data = r.json()
#Save ID and difficulty
questions = []
for q in data["stat_status_pairs"]:
    #print(q["stat"]["frontend_question_id"])
    questions.append({
                      "id": q["stat"]["frontend_question_id"],
                      "difficulty": q["difficulty"]["level"],
                      "backend_id": q["stat"]["question_id"]
                      })

questions.sort(key=lambda question: question["id"])
with open(FILE, 'w') as outfile:
    json.dump(questions, outfile)
#pp.pprint(questions)


