import random
import string
import re
import backendalgo
import tesaurus
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
stopword = StopWordRemoverFactory().create_stop_word_remover()
stemmer = StemmerFactory().create_stemmer()

def makedata():
	datall = []
	dataoutp = []
	listsin = []
	file = open("pertanyaan.txt", "r")
	dataoutp = file.readlines()
	for x in dataoutp:
		(index, pertanyaan, jawaban) = parsestring(x)
		datall.append((pertanyaan, jawaban))
		pertanyaanlist = pertanyaan.split(' ')
		for x in range(len(pertanyaanlist)):
			listsin = tesaurus.getSinonim(pertanyaanlist[x])
			if(len(listsin) != 0):
				for y in listsin:
					pertanyaanlist[x] = y
					datall.append((' '.join(pertanyaanlist), jawaban))
	#print(datall)
	return(datall)

def parsestring(stringlist):
	(index, plholder, stringpart) = stringlist.partition('.')
	stringlist = stringpart.strip()
	(pertanyaan, useless, jawaban) = stringlist.partition('?')
	jawaban = jawaban.strip()
	#print(pertanyaan, end = '#\n')
	#print(jawaban, end = '#\n')
	return(index, pertanyaan, jawaban)

def cariquery(string, datall):
	ret = []
	found = False
	indexpilihan = []
	for x in range(len(datall)):
		floatKMP = backendalgo.KMP(string, datall[x][0])
		floatBM = backendalgo.BM(string, datall[x][0])
		floatregex = backendalgo.regexmatch(string, datall[x][0])
		floatused = max([floatKMP, floatBM, floatregex])
		if(80 < floatused):
			ret = x
			indexpilihan.append((x, floatused))
			found = True
	if(found):
		return(indexpilihan, found)
	else:
		return(indexpilihan, found)

def backupcariquery(datall):
	keywordlist = []
	for x in datall:
		tempquestion = stemmer.stem(x[0])
		tempquestion = stopword.remove(tempquestion)
		keywordlist.append(tempquestion.split(' '))
	#print(keywordlist)
	return(keywordlist)

def backupsearch(string, backupq):
	keystring = []
	confkey = []
	string = stemmer.stem(string)
	string = stopword.remove(string)
	keystring = string.split(' ')
	print(keystring)
	for y in range(len(backupq)):
		cnt = 0
		for x in keystring:
			if(x in backupq[y]):
				cnt += 1
		confkey.append(cnt)
	indexmax = confkey.index(max(confkey))
	#print(confkey)
	#print(confkey[indexmax])
	#print(len(confkey)/len(keystring))
	if(len(confkey)/len(keystring) > 0.5):
		return(indexmax)
	else:
		return(-1)


def queryhandling(backupq, datall, stringinp, boolfound, indexpilihan):
	#print(indexpilihan)
	if(boolfound):
		print("pertanyaan pengguna :")
		print(stringinp)
		print("pertanyaan tersimpan : ")
		for x in range(0, min(3, len(indexpilihan))):
			print(indexpilihan)
			print(datall[indexpilihan[x][0]][0])
			print("jawaban : ")
			print(datall[indexpilihan[x][0]][1])
	else:
		indexbackup = backupsearch(stringinp, backupq)
		if(indexbackup != -1):
			print(datall[indexbackup][1])
		else:
			print("U wot m8?")

def main():
	'''
	CONTOH CARA PAKAI:

	'''
	indexpilihan = []
	datall = makedata()
	backupq = backupcariquery(datall)

	print("Halo, selamat datang")
	while 1:
		print(">" , end = '')
		stringinp = input()
		(indexpilihan, boolfound)  = cariquery(stringinp, datall)
		queryhandling(backupq, datall, stringinp, boolfound, indexpilihan)

main()