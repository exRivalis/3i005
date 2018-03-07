import math
import numpy as np

def occurence(proteine, a, i):
	# retourne le nombre d'occurences d'acide aminee a en position (colonne)i
	# proteine est une matrice L*M
	# a acide aminee
	# supposons que proteine soit un tableau de tableaux
	# pour chaque tableau on recup la case i
	cpt = 0
	for l in proteine:
		b = l[i]
		for x in b:
			for y in a:
				if x != y:
					break
		cpt+=1
	return cpt

def poid(proteine, a, i, q):
	# a acide aminee
	# poids
	# M nombre total de sequences
	# q tq les wi(a) forment la matrice de taille L*q
	# on suppose proteine tableau de tableaux
	M = len(proteine)
	return (occurence(proteine, a, i) + 1)/(M+q)

def entropie(proteine, q, i):
	# Si = log2(q) + sum a dans A (wi(a).log2[wi(a)])
	# A tout les acides en position i
	A = [l[i] for l in M]
	somme = 0

	for a in A:
		wi = poids(proteine, a, i, q)
		somme += wi * math.log2(wi)

	return math.log2(q) + somme

# np.argmax(a) retourne les indices des valeurs maximales
