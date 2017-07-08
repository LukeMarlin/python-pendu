import random
import string
import os

# On ouvre un fichier de mots FR avec lesquels on va jouer
#dico_mots = open("dictionnaire_francais.txt")

liste_mots = ["eyélàè"]

# On met chaque mot du dico dans une liste
#for each_mot in dico_mots:
#	mot = each_mot.strip()
#	liste_mots.append(mot)

# On prépare une liste qui enregistrera toutes les lettres essayées
liste_lettres_testees = []

# On commence par choisir un mot aléatoire de la liste
mot_random = random.choice(liste_mots)

nb_lettre_mot = len(mot_random)
print("Le mot sélectionné contient", nb_lettre_mot, "lettres.")

# On masque le mot à deviner pour le joueur
mot_cache = nb_lettre_mot * "-"
print("A toi de jouer coco :", mot_cache)

# On transforme le mot caché en liste pour pouvoir remplacer la lettre trouvée
mot_cache = list(mot_cache)

# On définit les caractères qui peuvent être proposés
# On définit une table de correspondance pour que dire à = a, é = e, etc...
correspondance = {
    'a': 'aàäâæ',
    'c': 'cç',
    'e': 'eêèéëæœ',
    'i': 'iîï',
    'o': 'oôöœ',
    'u': 'uùüû'
}
# .ascii-letters prend à la fois minuscule et majuscules
lettres_possibles = list(string.ascii_letters)

# On définit le nombre de tentatives
nb_tentatives = 10 


# Au début, le mot n'est pas encore trouvé
mot_trouve = False

# Tant que le mot n'a pas été trouvé, on demande de rentrer une lettre 
while not mot_trouve and (nb_tentatives > 0):

	# Si le mot est trouvé (plus de - dedans), on stope la boucle
	if not "-" in mot_cache:
		mot_trouve = True
		print("Tu pèses gros !")
		break

	# S'il n'est pas trouvé, on demande de rentrer une lettre
	lettre_proposee = input("Propose une lettre (sans accent) : ")

	# A voir si on ne le remonte pas d'un cran
	os.system("clear")

	# Si y'a pas qu'une seule lette OU que pas de lettre du tout
	if (len(lettre_proposee) > 1) or (not lettre_proposee) or (lettre_proposee not in lettres_possibles):
		print("Une lettre j'ai dit, baltringue !")
		print("".join(mot_cache))
		print("Nombre de tentatives restantes :", nb_tentatives)
		print("Tu as déjà proposé ces lettres :", liste_lettres_testees)
		# On revient au début de la boucle while
		continue

	# On regarde si la lettre proposée ne l'a pas déjà été, si oui, on en redemande une !
	if lettre_proposee in liste_lettres_testees:
		print("Tu as déjà proposé la lettre :", lettre_proposee)
		print("".join(mot_cache))
		print("Nombre de tentatives restantes :", nb_tentatives)
		print("Tu as déjà proposé ces lettres :", liste_lettres_testees)
		continue

	# On déclare une variable pour enregistrer soit la lettre proposée, soit la lettre proposée + toutes ses variables si elle a
	lettres = lettre_proposee

	if lettre_proposee in correspondance.keys():
		lettres = correspondance[lettre_proposee]
	
	lettre_trouvee = False

	# Pour chaque lettre proposée (lettre de base et éventuellement variantes)	
	for each_lettre in lettres:

		# On regarde si elle est dans le mot
		if each_lettre in mot_random:
		
			lettre_trouvee = True

			# Enumerate permet de voir l'index de chaque lettre > utile pour les doublons
			# On récupère chaque lettre (ou variante) du mot et sa position associée
			for index, lettre in enumerate(mot_random):

				# On vérifie que la lettre proposée a un équivalent dans le mot
				if each_lettre == lettre:
					# On remplace le tiret du bon index par la lettre
					mot_cache[index] = each_lettre

	if lettre_trouvee:
		# On repasse la liste en string en joignant chaque lettre					
		print("Continue comme ça !")
		print("".join(mot_cache))
		print("Nombre de tentatives restantes :", nb_tentatives)

	# Si la lettre proposée n'est pas dans le mot à trouver
	else:
		print("Caramba, encore raté !")
		print("".join(mot_cache))
		# On met à jour le nombre d'essais possibles
		nb_tentatives = nb_tentatives - 1
		if nb_tentatives == 0:
			rint("".join(mot_cache))
			print("Pendu ! Try again bro.")
			break
		else:
			print("Nombre de tentatives restantes :", nb_tentatives)


	# On ajoute la lettre à la liste de toutes les lettres déjà proposées
	liste_lettres_testees.append(lettre_proposee)
	print("Tu as déjà proposé ces lettres :", liste_lettres_testees)




