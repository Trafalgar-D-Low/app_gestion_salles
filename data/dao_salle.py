import json
import os
import mysql.connector
from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connexion