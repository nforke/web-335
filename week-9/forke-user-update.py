#/*
#===============================================
#; Title: Assignment 9.3
#; Author: Nicole Forke
#; Date: 25 June 2020
#; Modified By: Nicole Forke
#; Description: Updating and Deleting Documents
#===============================================
#*/

#// import statements

from pymongo import MongoClient

import pprint

import datetime

#// connect to local MongoDB database
client = MongoClient('localhost', 27017)

db = client.web335

#// update user document in database
db.users.update_one(
  {"employee_id": "000234"},

  #// update email address
  {
    "$set": {
      "email": "nforke@my365.bellevue.edu"
    }
  }
)

#// query the user collection
pprint.pprint(db.users.find_one(
  {
    "email": "nforke@my365.bellevue.edu",
    "employee_id": "000234",
    "first_name": "Melanie",
    "last_name": "Jones"
  }
))