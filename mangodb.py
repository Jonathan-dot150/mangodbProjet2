






from pymongo import MongoClient
import csv

# connexion Atlas
client = MongoClient("mongodb+srv://joo150_db_user:Broccoli123@cluster0.nti1pod.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# base + collection
db = client["ma_base"]
collection = db["ma_collection"]

# lire CSV et insérer
with open("monfichier.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        collection.insert_one(row)

print("Import terminé ✅")


