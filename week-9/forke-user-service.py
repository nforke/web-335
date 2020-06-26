#/*
#===============================================
#; Title: Assignment 9.2
#; Author: Nicole Forke
#; Date: 25 June 2020
#; Modified By: Nicole Forke
#; Description: Querying and Creating Documents
#===============================================
#*/

#// import statements

from pymongo import MongoClient

import pprint

import datetime

#// connect to local MongoDB database
client = MongoClient('localhost', 27017)

db = client.web335

#// new user document
user = {
  "first_name": "Melanie",
  "last_name": "Jones",
  "email": "mel@email.com",
  "employee_id": "000234",
  "date_created": datetime.datetime.utcnow()
}

#// insert user document
user_id = db.users.insert_one(user).inserted_id

#// output the auto-generated user_id
print(user_id)

#// query the users collection
employee_id = "000234"

pprint.pprint(db.users.find_one({"employee_id":"000234"}))