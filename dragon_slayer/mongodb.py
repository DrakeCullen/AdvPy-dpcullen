from pymongo import MongoClient, MongoClient
import pymongo

def get_database():
    CONNECTION_STRING = "mongodb+srv://testUser:test123@cluster0.xa5sn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db = client['dragonSlayer']
    return db['Leaderboard']

def insert_db(db, name, score):
    db.insert_one({"Name" : name, "Score": score})

def get_top_five(db):
    return db.find().sort("Score", -1).limit(5)
    
if __name__ == "__main__":    
    dragonSlayer = get_database()
    res = get_top_five(dragonSlayer)
    for x in res:
        print(x["Name"], x["Score"])
