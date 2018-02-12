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

def liste_longueur(lem):
	li=[]
	for l in lem:
		li.append(longueur_body(l))
		
	return li
	
plt.hist(liste_longueur(l1),bins=100)
plt.show()
