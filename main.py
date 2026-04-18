from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

# Ajouter une salle
s1 = Salle("B205", "Labo INFO", "Laboratoire", 20)
resultat, msg = service.ajouter_salle(s1)
print(msg)

# Lister toutes les salles
print("\n------------Liste des salles------------")
for salle in service.recuperer_salles():
    salle.afficher_infos()

# Modifier une salle
s1.description = "Labo modifié"
resultat, msg = service.modifier_salle(s1)
print(msg)

# Rechercher une salle
print("\n------------Recherche B205------------")
trouve = service.rechercher_salle("B205")
if trouve:
    trouve.afficher_infos()

# Supprimer une salle
service.supprimer_salle("B205")
print("Salle supprimée!")
