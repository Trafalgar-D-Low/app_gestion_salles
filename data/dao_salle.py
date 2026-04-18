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

    def insert_salle(self, salle):
        cnx = self.get_connection()
        curseur = cnx.cursor()
        curseur.execute(
            "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)",
            (salle.code, salle.description, salle.categorie, salle.capacite))
        cnx.commit()
        curseur.close()
        cnx.close()

    def update_salle(self, salle):
        cnx = self.get_connection()
        curseur = cnx.cursor()
        curseur.execute(
            "UPDATE salle SET description = %s, categorie = %s, capacite = %s WHERE code = %s",
            (salle.description, salle.categorie, salle.capacite, salle.code)
        )
        cnx.commit()
        curseur.close()
        cnx.close()