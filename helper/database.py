import pymongo 
import os
import datetime
import motor.motor_asyncio
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
ADMIN = int(os.environ.get("ADMIN", 1391556668))

DB_NAME = os.environ.get("DB_NAME","")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["USER"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"lg_code":None}
            try:
            	dbcol.insert_one(user_det)
            except:
            	pass

def set(chat_id,lg_code):
	 dbcol.update_one({"_id":chat_id},{"$set":{"lg_code":lg_code}})

	 	
def unset(chat_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"lg_code":None}})

def find(chat_id):
	id =  {"_id":chat_id}
	x = dbcol.find(id)
	for i in x:
             lgcd = i["lg_code"]
             return lgcd 

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values

def find_one(id):
	return dbcol.find_one({"_id":id})

def full_userbase():
    user_docs = dbcol.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids
 
class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user

    def new_user(self, id):
        return dict(
            _id=int(id),
            join_date=datetime.date.today().isoformat()
        )

    async def add_user(self, b, m):
        u = m.from_user
        if not await self.is_user_exist(u.id):
            user = self.new_user(u.id)
            await self.col.insert_one(user)            
            await send_log(b, u)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'_id': int(user_id)})

db = Database(DB_URL, DB_NAME)
