import pymongo
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
students = db.students


def average(students):
    for student in students.find() :
        score_table = [ float(s['score']) for s in student['scores']]
        min_score = min(score_table)
        
        #students.update({'_id':student['_id']},{'$pull':{'scores.score':min_score}})
        avg=(sum(score_table)/len(score_table))
        yield(student['_id'],avg) 



for student in students.find() :
    score_table = [ float(s['score']) for s in student['scores']]
    min_score = min(score_table)
    students.update({'_id':student['_id']},{'$pull':{'scores.score':min_score}})




        
