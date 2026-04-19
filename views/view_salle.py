import customtkinter as ctk
from tkinter import ttk, messagebox
from models.salle import Salle
from services.services_salle import ServiceSalle

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Gestion des salles"
        self.geometry = "600x600"
        self.service_salle = ServiceSalle()
        self.resizable(False, False)
        self.configure(fg_color="#1a1a2e")

        # cadre Informations Salle
        self.cadreInfo = ctk.CTkFrame(self, fg_color="#16213e", corner_radius=10, border_width=1, border_color="#7b2d8b")
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.cadreInfo, text="Code :", text_color="#c77dff", fg_color="#16213e").grid(row=0, column=0, padx=15, pady=8, sticky="e")
        self.entry_code = ctk.CTkEntry(self.cadreInfo, fg_color="#0f3460", border_color="#7b2d8b", text_color="white")
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Description :", text_color="#c77dff", fg_color="#16213e").grid(row=1, column=0, padx=15, pady=8, sticky="e")
        self.entry_description = ctk.CTkEntry(self.cadreInfo, fg_color="#0f3460", border_color="#7b2d8b", text_color="white")
        self.entry_description.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Catégorie :", text_color="#c77dff", fg_color="#16213e").grid(row=2, column=0, padx=15, pady=8, sticky="e")
        self.entry_categorie = ctk.CTkEntry(self.cadreInfo, fg_color="#0f3460", border_color="#7b2d8b", text_color="white")
        self.entry_categorie.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.cadreInfo, text="Capacité :", text_color="#c77dff", fg_color="#16213e").grid(row=3, column=0, padx=15, pady=8, sticky="e")
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo, fg_color="#0f3460", border_color="#7b2d8b", text_color="white")
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)

        # cadre Actions
        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10)

        self.btn_ajouter = ctk.CTkButton(self.cadreActions, text="Ajouter", fg_color="#7b2d8b", hover_color="#9d4edd", text_color="white", corner_radius=8, command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreActions, text="Modifier", fg_color="#7b2d8b", hover_color="#9d4edd", text_color="white", corner_radius=8, command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreActions, text="Supprimer", fg_color="#7b2d8b", hover_color="#9d4edd", text_color="white", corner_radius=8, command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreActions, text="Rechercher", fg_color="#7b2d8b", hover_color="#9d4edd", text_color="white", corner_radius=8, command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

        # cadre Liste des salles
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10)
        self.treeList = ttk.Treeview(self.cadreList, columns=("code", "description", "categorie", "capacite"), show="headings")

        # En-têtes
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        # Largeur des colonnes
        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        # charger la liste au démarrage
        self.lister_salles()

    def ajouter_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()
        try:
            capacite = int(capacite)
        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre entier!")
            return
        salle = Salle(code, description, categorie, capacite)
        ok, msg = self.service_salle.ajouter_salle(salle)
        messagebox.showinfo("Info", msg)
        if ok:
            self.lister_salles()

    def modifier_salle(self):
        code = self.entry_code.get()
        description = self.entry_description.get()
        categorie = self.entry_categorie.get()
        capacite = self.entry_capacite.get()
        try:
            capacite = int(capacite)
        except ValueError:
             messagebox.showerror("Erreur", "La capacité doit être un nombre entier!")
             return
        salle = Salle(code, description, categorie, capacite)
        ok, msg = self.service_salle.modifier_salle(salle)
        messagebox.showinfo("Info", msg)
        if ok:
            self.lister_salles()

    def supprimer_salle(self):
        code = self.entry_code.get()
        if not code:
            messagebox.showerror("Erreur", "Veuillez entrez un code!")
            return
        self.service_salle.supprimer_salle(code)
        messagebox.showinfo("Info", "Salle supprimée.")
        self.lister_salles()

    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)
        if salle:
            self.entry_code.delete(0, "end")
            self.entry_code.insert(0, salle.code)
            self.entry_description.delete(0, "end")
            self.entry_description.insert(0, salle.description)
            self.entry_categorie.delete(0, "end")
            self.entry_categorie.insert(0, salle.categorie)
            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, str(salle.capacite))
        else:
            messagebox.showerror("Erreur", "Salle non trouvée!")

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))
