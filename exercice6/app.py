from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB (nom du service défini dans docker-compose)
client = MongoClient("mongodb://mongodb:27017/")

# On choisit une base et une collection
db = client["testdb"]
collection = db["messages"]

@app.route("/")
def hello():
    # Insertion d’un document
    collection.insert_one({"message": "Hello from Flask & MongoDB!"})

    # Lecture du dernier message
    last_msg = collection.find().sort("_id", -1).limit(1)[0]["message"]
    return f"Message enregistré et lu depuis MongoDB : {last_msg}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
