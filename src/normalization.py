#####################
#학생정규화
#####################


import pymongo
import sys
import os
import re

TITLE = sys.argv[1]
NUMBER = sys.argv[2]
STUDENT = sys.argv[3]

Path = "../Student/"+TITLE+"/"+STUDENT+"/"

connection = pymongo.MongoClient()

db = connection.get_database("cprog")
collections = db.get_collection("boards")
collection = collections.find({"title":TITLE})
col = collection.distinct("subquestion")
comp = "".join(col)
comp = comp.split(',')

for i in range(1,int(NUMBER)+1):
	if comp[i-1] == 'T' :
		f = open(Path+str(i)+'.log','r+')
		line = f.read()
		pattern = re.compile(r'\s+')
		change = re.sub('[=.#/@!?:$%^}]', '',line)
		change = re.sub(pattern, '', change)
		f.seek(0)
		f.write(change)
		f.truncate()
		f.close()
		os.rename(Path+str(i)+'.log',Path+'output_'+str(i)+'.log')
	else :
		os.rename(Path+str(i)+'.log',Path+'output_'+str(i)+'.log')
