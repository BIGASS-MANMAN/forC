import pymongo
import sys
import os
import re


TITIL = sys.argv{1}
NUMBER = sys.argv{2}
STUDENT = sys.argv{3}

Path = "../Assistant/"+TITLE

connection = pymongo.MongoClient()
db = connection.get_database("cprog")
collections = db.get_collection("question")
collection = collections.find({"Title":Title})
col = collection.distinct("SubQuestion")

for i in range(1, NUMBER+1):
	if col[0][str(i)] :
		f = open(Path+str(i)+'.log','r+')
		line = f.read()
		pattern = re.compile(r'\s+')
		change = re.sub('[=.#/@!?:$%^}]', '',line)
		change = re.sub(pattern, '', change)
		f.seek(0)
		f.write(change)
		f.truncate()
		f.close()
		os.rename(Path+str(i)+'.log',Path+'expected_'+str(i)+'.log')
	else :
		os.rename(Path+str(i)+'.log',Path+'expected_'+str(i)+'.log')
