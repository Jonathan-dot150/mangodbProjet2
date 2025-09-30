






from pymongo import MongoClient
import csv

# connexion Atlas
client = MongoClient("mongodb+srv://joo150_db_user:Broccoli123@cluster0.nti1pod.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# base + collection
db = client["bestbuy"]
collection = db["electronique"]




