import sys
import os
import pymongo

TITLE = sys.argv[1]
NUMBER = sys.argv[2]
STUDENT = sys.argv[3]

Path = "../Student/"+TITLE+"/"+STUDENT
Path2 = "../Assistant/"+TITLE

connection = pymongo.MongoClient()
db = connection.get_database("cprog")
col_question = db.get_collection("question")
col_result = db.get_collection("result")
question_info = col_question.find({"Title" : TITLE})

Subquestion_info = question_info[0]["SubQuestion"]
SubCount = question_info[0]["Cnt"]

f = {}
f2 = {}
result = {}
for i in range(1,int(NUMBER)+1):
	file_name = os.path.join(Path,"output_"+str(i)) + ".log"
	file_name2 = os.path.join(Path2,"expected_"+str(i)) + ".log"
	#예외처리 필요(file_name) open 못하는 것 list로 관리
	if os.path.exists(file_name):
		f[i] = open(file_name,"r")
	else:
		f[i] = False
	if os.path.exists(file_name2):
		f2[i] = open(file_name2,"r")


for i in range(1,int(NUMBER)+1):
	if f[i] == False:
		result[str(i)] = False
		print("False")
	else:
		while True:
			line = f[i].readline()
			line2 = f2[i].readline()
			if line != line2 :
				result[str(i)] = False
				break
			if not line or not line2 :
				result[str(i)] = True
				break

Result = {"Title" : TITLE, "Cnt" : int(NUMBER), "Result" : result, "ID" : STUDENT}
col_result.insert(Result)

	
print(result)
print(SubCount)
