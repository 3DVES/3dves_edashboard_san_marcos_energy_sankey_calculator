from pymongo import MongoClient
from datetime import datetime, timedelta

Client = MongoClient("mongodb://172.31.43.75:27017/")#("mongodb://52.36.190.119:27017/")
db = Client["sanmarcos"]
col = db["attributes"]
col2 = db["attributehistories"]


def attribute_current_value(ide):
    for document in col.find({"_id": ide}):
        return document["currentValue"]


def attribute_value(ide):
    for document in col2.find({"_id": ide}):
        return document["value"]


def search_histories(ide, dat):
    for document in col2.find({"attributeId": ide}):
        if str(document["date"])[0:10] == str(dat)[0:10]:
            return document["_id"]


def sum_last_360_days(ide):
    dt = datetime.now()
    sum = 0
    while str(dt)[0:10] >= str(datetime.now() - timedelta(days=360)):
        ID = search_histories(ide, dt)
        sum = sum + float(attribute_value(ID))
        dt = dt - timedelta(days=30)
    return sum


def sum_year2(col, ide):
    dt = datetime(2021, 7, 1)
    sum = 0
    while str(dt)[0:10] >= str(datetime.now() - timedelta(days=360))[0:10]:
        ID = search_histories(col, ide, dt)
        sum = sum + float(attribute_value(col, ID))
        dt = dt - timedelta(days=30)
    return sum
