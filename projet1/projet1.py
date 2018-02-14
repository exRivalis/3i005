import email
import re
import math
import numpy as np
import matplotlib.pyplot as plt

def read_file(fname):
    """ Lit un fichier compose d'une liste de emails, chacun separe par au moins 2 lignes vides."""
    f = open(fname,'rb')
    raw_file = f.read()
    f.close()
    raw_file = raw_file.replace(b'\r\n',b'\n')
    emails =raw_file.split(b"\n\n\nFrom")
    emails = [emails[0]]+ [b"From"+x for x in emails[1:] ]
    return emails

def get_body(em):
    """ Recupere le corps principal de l'email """
    body = em.get_payload()
    if type(body) == list:
        body = body[0].get_payload()
    try:
        res = str(body)
    except Exception:
        res=""
    return res

def clean_body(s):
    """ Enleve toutes les balises html et tous les caracteres qui ne sont pas des lettres """
    patbal = re.compile('<.*?>',flags = re.S)
    patspace = re.compile('\W+',flags = re.S)
    return re.sub(patspace,' ',re.sub(patbal,'',s))

def get_emails_from_file(f):
    mails = read_file(f)
    return [ s for s in [clean_body(get_body(email.message_from_bytes(x))) for x in mails] if s !=""]

spam = get_emails_from_file("spam.txt" )
nospam = get_emails_from_file("nospam.txt")

"""
for s in spam:
	print (s)
"""

def split(liste, x):
	l1 = []
	l2 = []
	pivot = math.floor(len(liste)*x)
	
	l1 = liste[0:pivot]
	l2 = liste[pivot:]
	
	return l1, l2

l1,l2=split(spam, 0.2)

#np.bin

def longueur_body(em):

	return len(em)
	
print(longueur_body(l1[0]))

#pour calculer l'histogramme des longeur de mails
def liste_longueur(lem):
	li=[]
	for l in lem:
		li.append(longueur_body(l))
		
	return li
"""
liste = liste_longueur(l1)
length = len(liste)
plt.hist(liste,bins=int(length/20))
"""
#Q 2.3
def apprend_modele(spam, non_spam):
	#renvoie la proba qu'un email soit d'une longueur donnée sachant que c'est un spam
	#p(X=x | Y=+1) = p(Y=+1 | X=x) * p(X=x) / p(Y=+1)
	#or p(Y=+1) = 0.5
	#et p(X=x) = nbr email de longueur x / nbr email
	#et p(Y=+1 | X=x) = nbr email spam de taille x / nbr longueur de taille x
	
	#renvoyer la distribution des spam selon leur longueur x
	
	#calculs:
	#suppression des doublons dans les listes
	liste_mails = list(set(spam+non_spam))
	#tableau (longueur, proba)
	dict_lp = {} #dictionnaire longueur, proba spam
	
	for x in liste_mails:
		dict_lp[x] = distribution(spam, non_spam, x)
	
	return dict_lp
	

def distribution(spam, non_spam, x):
	#renvoie p(X=x | Y=+1) pour une longueur x donnee
	nb_x_spam = 0 #nbre de spam de longueur x
	nb_x_tot = 0 #nbre total de mail de llongueur x
	
	for lm in spam:
		if lm == x:
			nb_x_spam += 1
			nb_x_tot += 1
	for lm in non_spam:
		if lm == x:
			nb_x_tot += 1
	
	px = float(nb_x_tot) / (nb_x_tot + nb_x_spam) #p(X=x)
	pyx = float(nb_x_spam) / nb_x_tot #p(Y=+1 | X=x)
	
	pxy = pyx * px / 0.5 #p(X=x | Y=+1)
	
	return pxy
	
def predict_email(emails, modele):
	#renvoie la liste des labels pour l'ensemble des emails en fonction du modele passe en parametre

	labels = [] #labels[i] contient le label de l'email emails[i]
	for e in emails:
		longueur = longueur_body(e)
		if modele[longueur] > 0.5:
			labels.append(+1)
		else:
			labels.append(-1)
	
	return labels
	

	
plt.show()
