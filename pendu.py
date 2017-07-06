import random
import string

# On définit une liste de mots avec lesquels on va jouer
liste_mot = ["énèagrämmù"]

# On prépare une liste qui enregistrera toutes les lettres essayées
liste_lettres_testees = []

# On commence par choisir un mot aléatoire de la liste
mot = random.choice(liste_mot)

nb_lettre_mot = len(mot)
print("Le mot sélectionné contient", nb_lettre_mot, "lettres.")

# On masque le mot à deviner pour le joueur
mot_cache = nb_lettre_mot * "-"
print("A toi de jouer coco :", mot_cache)

# On transforme le mot caché en liste pour pouvoir remplacer la lettre trouvée
mot_cache = list(mot_cache)

# On définit les caractères qui peuvent être proposés
lettres_accents = ["à", "é", "è", "ë", "ö", "ù", "ï"]
lettres_possibles = list(string.ascii_lowercase) + list(string.ascii_uppercase) + lettres_accents

# Au début, le mot n'est pas encore trouvé
mot_trouve = False

# Tant que le mot n'a pas été trouvé, on demande de rentrer une lettre 
while not mot_trouve:

	# Si le mot est trouvé (plus de - dedans), on stope la boucle
	if not "-" in mot_cache:
		mot_trouve = True
		print("Tu pèses gros !")
		break

	# S'il n'est pas trouvé, on demande de rentrer une lettre
	lettre_proposee = input("Propose une lettre : ")

	# Si y'a pas qu'une seule lette OU que pas de lettre du tout
	if (len(lettre_proposee) > 1) or (not lettre_proposee) or (lettre_proposee not in lettres_possibles) :
		print("Une lettre j'ai dit, baltringue !")
		# On revient au début de la boucle while
		continue

	if lettre_proposee in liste_lettres_testees:
		print("Tu as déjà proposé la lettre :", lettre_proposee)
		continue

	# On regarde si la lettre proposée ne l'a pas déjà été, et qu'elle est dans le mot à trouver
	if (lettre_proposee not in liste_lettres_testees) and (lettre_proposee in mot) :
		occurence_lettre_proposee = mot.count(lettre_proposee)
		print("GG, t'as trouvé une des lettres. Le mot contient", occurence_lettre_proposee, "fois la lettre", lettre_proposee)

		# Enumerate permet de voir l'index de chaque lettre > utile pour les doublons
		for index, lettre in enumerate(mot):
			
			if lettre == lettre_proposee:
				index_lettre_proposee = index
				# On remplace le tiret du bon index par la lettre
				mot_cache[index_lettre_proposee] = lettre_proposee

		# On repasse la liste en string en joignant chaque lettre					
		print("Continue comme ça !", "".join(mot_cache))

	# Si la lettre proposée n'est pas dans le mot à trouver
	else:
		print("Caramba, encore raté !")

	liste_lettres_testees.append(lettre_proposee)


