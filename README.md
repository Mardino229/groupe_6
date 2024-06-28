# groupe_6
TP Python

Tâche 1 

numpy.py définit une classe Python appelée Array qui représente un tableau multidimensionnel, offrant des fonctionnalités de base pour les opérations mathématiques.

Fonctionnalités de la classe:

Initialisation:

Le constructeur __init__ prend une liste d'entiers ou une liste de listes d'entiers comme entrée, représentant le tableau.
Il détermine la dimension du tableau (1D ou 2D) et stocke la forme dans l'attribut shape.

Opérations mathématiques:

Addition (__add__): Permet d'ajouter un autre tableau, un entier ou un flottant au tableau courant. Gère les cas 1D et 2D et vérifie la compatibilité des dimensions.

Multiplication (__mul__): Permet de multiplier un autre tableau, un entier ou un flottant au tableau courant. Gère les cas 1D et 2D et vérifie la compatibilité des dimensions.

Soustraction (__sub__): Permet de soustraire un autre tableau, un entier ou un flottant au tableau courant. Gère les cas 1D et 2D et vérifie la compatibilité des dimensions.

Division (__truediv__): Permet de diviser un autre tableau, un entier ou un flottant au tableau courant. Gère les cas 1D et 2D et vérifie la compatibilité des dimensions. Vérifie également la division par zéro.

Produit scalaire (__matmul__): Permet de calculer le produit scalaire de deux tableaux 1D de même longueur.

Autres fonctionnalités:

Appartenance (__contains__): Vérifie si une valeur donnée est présente dans le tableau.

Accéder aux éléments (__getitem__): Permet d'accéder aux éléments du tableau en utilisant des index ou des tranches, supportant les index uniques, les tranches et les index multiples pour les tableaux 2D.

Représentation (__repr__): Retourne une représentation textuelle du tableau.

Longueur (__len__): Retourne le nombre d'éléments en 1D, et nombre de lignes en 2D.

Points importants:

Le code gère les cas 1D et 2D avec des boucles imbriquées pour les opérations.
Il utilise des ValueError et des TypeError pour gérer les erreurs lors des opérations.
Les opérations mathématiques sont définies en utilisant les opérateurs spéciaux de Python (+, *, -, /, @).
Le code contient des commentaires pour expliquer les différentes sections.

Conclusion:

Ce fichier offre une implémentation d'une classe Array avec des fonctionnalités de base pour les opérations mathématiques sur des tableaux multidimensionnels. Il est bien structuré, clair et facile à comprendre. Le code gère les erreurs et propose des commentaires explicatifs.

Tâche 2 

Voici l'analyse du graphe "Histogramme des nombres de chambres"

#la plupart des propriétés dans le dataset ont 2 ou 3 chambres, avec un pic notable à 3 chambres (environ 300 propriétés). Les maisons avec moins de 2 chambres ou plus de 4 chambres sont beaucoup moins fréquentes.

Voici l'analyse du graphe "Scatter Plot de Area vs Price"

#Le nuage de points indique que, bien que la taille de la propriété soit un facteur important pour déterminer le prix, d'autres variables jouent également un rôle significatif. Les prix des propriétés peuvent varier considérablement pour des surfaces similaires, et quelques propriétés de luxe ou dans des zones premium montrent des prix particulièrement élevés.

Tâche 3

app.py est un programme simple qui utilise l'interface utilisateur tkinter pour créer un générateur d'images basique basé sur Stable Diffusion.

Voici une description détaillée :

Importations:

tkinter: Permet de créer l'interface graphique.
threading: Permet de créer des threads pour exécuter des tâches en arrière-plan.

os: Permet d'interagir avec le système d'exploitation (ici, pour supprimer un fichier).

diffusers: Permet de charger et d'utiliser le modèle Stable Diffusion.

PIL: Permet de manipuler des images.

Variables globales:

width, height: Définissent la taille du canvas pour l'image générée.

spinner_label: Stocke l'objet label pour l'affichage de l'indicateur de chargement.

spinner_states: Contient les différents états de l'indicateur (charactères de spin).

current_state: Indique l'état actuel de l'indicateur.
spinner_running: Indique si l'indicateur est en cours d'exécution.
Fonctions:

start_spinner(): Commence l'animation de l'indicateur de chargement en changeant l'état du label à intervalles réguliers.
stop_spinner(): Arrête l'animation de l'indicateur et met le label à "Chargement terminé".
generate_image(): Cette fonction gère la génération de l'image. Elle :
Lance start_spinner() pour activer l'indicateur de chargement.
Récupère la description de l'image saisie par l'utilisateur.
Charge le modèle Stable Diffusion.
Génère l'image avec la description saisie.
Enregistre l'image dans un fichier "generated_image.png".
Affiche l'image générée sur le canvas.
Lance stop_spinner() pour arrêter l'indicateur de chargement.
Crée un thread pour exécuter la génération de l'image en arrière-plan, permettant à l'interface de rester responsive.
Création de l'interface:

La fenêtre principale est créée avec Tk().
Le titre, la taille et la redimensionnabilité de la fenêtre sont configurés.
Un cadre (Frame) est créé pour contenir les éléments de l'interface.
Un titre ("IMAGE GENERATOR") est ajouté.
Un cadre pour le champ de saisie est créé.
Un label "Description:" est ajouté, suivi d'un champ de texte (Entry) pour la description de l'image.
Un bouton "Générer une Image" est ajouté, qui lance la fonction generate_image() lorsqu'il est cliqué.
Un label pour l'indicateur de chargement est ajouté.
Un canvas est créé pour afficher l'image générée.
Conclusion:

Ce programme offre une interface utilisateur simple pour générer des images avec Stable Diffusion. Il utilise un thread pour éviter de bloquer l'interface pendant le processus de génération.


Contribution de chaque membre de l'équipe :

Tâche 1:

Implémentation de la classe Array et méthode addition: 
  -DJOSSOU Will Sonagnon

Opérations arithmétique et scalaire : 
 -DASSI Maxime Mardino
 -METODJO Toundé Jean-Joel

Recherche d'éléments, Indexation et slicing : 
 -DASSI Maxime Mardino
 -FAHOUBO Dossou Rodrigue

Tâche 2:

hist.py et scatter.py :
 -DEGBEY Mahouna Baron Quiétude 
 -TEHOUENOU Sèdégbé Gédéon Espamour

hist.r et scatter.r : 
 -OKE Fèmi Michèl

Tâche 3 

Auteur: DASSI Maxime Mardino

Contribution en pourcentage:

1.DASSI Maxime Mardino : 21%
2.GBODO Chris Vianney Maoulé : 
3.METODJO Toundé Jean-Joel : 12%
4.DJOSSOU Will Sonagnon : 11%
5.LAOUROU Adebola : 
6.FAHOUBO Dossou Rodrigue : 2%
7.TEHOUENOU Sèdégbé Gédéon Espamour : 12%
8.DEGBEY Mahouna Baron Quiétude : 15%
9.OKE Fèmi Michèl : 15%
10.TCHEGNINOUGBO Sègbènou Hersuze Péniel : 12%
11.DOSSA Oscar : 

Voici l'analyse du graphe "Histogramme des nombres de chambres"

#la plupart des propriétés dans le dataset ont 2 ou 3 chambres, avec un pic notable à 3 chambres (environ 300 propriétés). Les maisons avec moins de 2 chambres ou plus de 4 chambres sont beaucoup moins fréquentes.

Voici l'analyse du graphe "Scatter Plot de Area vs Price"

#Le nuage de points indique que, bien que la taille de la propriété soit un facteur important pour déterminer le prix, d'autres variables jouent également un rôle significatif. Les prix des propriétés peuvent varier considérablement pour des surfaces similaires, et quelques propriétés de luxe ou dans des zones premium montrent des prix particulièrement élevés.



