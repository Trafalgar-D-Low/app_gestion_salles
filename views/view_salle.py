import customtkinter as ctk
from tkinter import ttk, messagebox
from models.salle import Salle
from services.services_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Gestion des salles"
        self.geometry = "600x600"
        self.service_salle = ServiceSalle()
