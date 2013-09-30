import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
students = db.students


def average(students):
    for student in students.find() :
        homework_table = [ float(s['score']) for s in student['scores'] if s['type'] == 'homework']
        min_score = min(homework_table)
        reduced_score_table = [h for h in homework_table if h > min_score]
        #students.update({'_id':student['_id']},{'$pull':{'scores.score':min_score}})
        avg=(sum(reduced_score_table)/len(reduced_score_table))
        yield(student['_id'],avg) 

#print(sorted(average(students),key=lambda k:k[1],reverse=True))

def lowest_homework(students=students):
    for student in students.find() :
        homework_table = [ float(s['score']) for s in student['scores'] if s['type'] == 'homework']
        min_score = min(homework_table)
        yield(student['_id'],min_score)
        
         

for (s_id,min_score) in lowest_homework(students):
    print(str(s_id)+" "+str(min_score))
    students.update({'_id':s_id},{'$pull':{'scores.score':min_score}})




        
