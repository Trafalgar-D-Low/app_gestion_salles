import json
import os
import mysql.connector
from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("data/config.json", "r", encoding="utf-8") as f:
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

    def delete_salle(self, code):
        cnx = self.get_connection()
        curseur = cnx.cursor()
        curseur.execute("DELETE FROM salle WHERE code = %s", (code,))
        cnx.commit()
        curseur.close()
        cnx.close()

    def get_salle(self, code):
        cnx = self.get_connection()
        curseur = cnx.cursor()
        curseur.execute("SELECT code, description, categorie, capacite FROM salle WHERE code = %s", (code,))
        ligne = curseur.fetchone()
        curseur.close()
        cnx.close()
        if ligne:
            return Salle(ligne[0], ligne[1], ligne[2], ligne[3])
        return None

    def get_salles(self):
        cnx = self.get_connection()
        curseur = cnx.cursor()
        curseur.execute("SELECT code, description, categorie, capacite FROM salle")
        lignes = curseur.fetchall()
        curseur.close()
        cnx.close()
        liste = []
        for ligne in lignes:
            liste.append(Salle(ligne[0], ligne[1], ligne[2], ligne[3]))
        return liste