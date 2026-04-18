from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
conn = dao.get_connection()
print("Connexion réussie :", conn)

# Ajouter une salle
s1 = Salle("A101", "Salle de TP", "TP", "25")
dao.insert_salle(s1)
print("Salle ajoutée !")

# Afficher toutes les salles
print("\n-------Liste des salles--------")
salles = dao.get_salles()
for s in salles:
    s.afficher_infos()

# Rechercher une salle
print("\n-------Salle A101--------")
s = dao.get_salle("A101")
if s :
    s.afficher_infos()

# Modifier une salle
s1.description = "Salle modifiée"
dao.update_salle(s1)
print("\nSalle modifiée !")

# Supprimer une salle
dao.delete_salle("A101")
print("Salle supprimée !")
