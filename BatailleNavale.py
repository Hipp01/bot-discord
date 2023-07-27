class BatailleNavale:
    def __init__(self, joueur1, joueur2):
        """
        Initialise une nouvelle partie de Bataille Navale.

        Parameters:
            joueur1 (str): Le nom du joueur 1.
            joueur2 (str): Le nom du joueur 2.
        """
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.grille_joueur1 = [[0] * 10 for _ in range(10)]  # Grille du joueur 1
        self.grille_joueur2 = [[0] * 10 for _ in range(10)]  # Grille du joueur 2
        self.navires_joueur1 = []  # Liste des navires du joueur 1
        self.navires_joueur2 = []  # Liste des navires du joueur 2
        self.tour_actuel = joueur1  # Le joueur dont c'est le tour
        self.joueur_gagnant = None  # Le joueur gagnant (None tant que le jeu n'est pas terminé)

    def placer_navire(self, joueur, navire, x, y, orientation):
        """
        Place un navire sur la grille du joueur.

        Parameters:
            joueur (str): Le nom du joueur.
            navire (str): Le nom du navire à placer.
            x (int): La coordonnée x du coin supérieur gauche du navire.
            y (int): La coordonnée y du coin supérieur gauche du navire.
            orientation (str): L'orientation du navire ('horizontal' ou 'vertical').

        Returns:
            bool: True si le placement est réussi, False sinon (si l'emplacement est invalide ou déjà occupé).
        """
        if joueur == self.joueur1:
            grille = self.grille_joueur1
            navires = self.navires_joueur1
        else:
            grille = self.grille_joueur2
            navires = self.navires_joueur2

        if x<=0 or x>10 or y<=0 or y>10:
            return False

        if orientation == "horizontal":
            if len(navire) + x > 10:
                return False
        elif orientation == "vertical":
            if len(navire) + y > 10:
                return False
        else:
            return False
        
    def afficher_grille(self, joueur):
        """
        Affiche la grille du joueur avec les navires et les tirs.

        Parameters:
            joueur (str): Le nom du joueur.
        """
        pass

    def tirer(self, joueur, x, y):
        """
        Effectue un tir sur la grille adverse.

        Parameters:
            joueur (str): Le nom du joueur effectuant le tir.
            x (int): La coordonnée x du tir.
            y (int): La coordonnée y du tir.

        Returns:
            str: Résultat du tir ('touché', 'coulé', 'manqué').
        """
        pass

    def est_partie_terminee(self):
        """
        Vérifie si la partie est terminée.

        Returns:
            bool: True si la partie est terminée, False sinon.
        """
        pass

    def obtenir_joueur_gagnant(self):
        """
        Renvoie le nom du joueur gagnant.

        Returns:
            str: Le nom du joueur gagnant, ou None si la partie n'est pas encore terminée.
        """
        pass
