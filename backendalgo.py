import random
import string
import re


#Algoritma KMP, inputnya substring sama string, return boolean
def KMP(substring, string):
	string = string.lower()
	substring = substring.lower()
	result = False
	pitable = []
	newpitable = []
	newpitable = [0]
	subsList = ['x']
	stringList = ['x']
	charcocok = 0
	tempcocok = 0
	pitable = KMPspindex(substring)
	
	for x in pitable:
		newpitable.append(x)
	for x in substring:
		subsList.append(x)
	for x in string:
		stringList.append(x)
	
	if(len(substring) == 0 or len(string) == 0):
		return(0)

	matchindex = -1
	i = 1
	j = 0
	found = False
	while(i < len(stringList)):
		if(subsList[j+1] == stringList[i]):
			if found:
				charcocok += 1
			else:
				if(tempcocok < charcocok):
					tempcocok = charcocok
				charcocok = 1
			found = True
			j += 1
			i += 1
		else:
			if(j == 0):
				i += 1
				found = False
			else:
				j = newpitable[j]
				found = False

		#compare success
		if(j + 1 == len(subsList)):
			result = True
			matchindex = i - len(substring)
			tempcocok = len(substring)
			break

	return(tempcocok/len(string) * 100)


#KMPspindex adalah fungsi yang digunakan pada KMP() untuk mencari pitable 
#yang digunakan dalam pencocokan suffix & prefix substring

def KMPspindex(substring):
	pitable = []
	for x in range(0, len(substring)):
		pitable.append(0)
	for x in range(1, len(substring)):
		if(substring[x] == substring[0] and pitable[x] == 0):
			pitable[x] = 1
			cnt = x
			i = 1
			if(cnt + i < len(substring)):
				while(substring[cnt + i] == substring[i]):
					pitable[cnt + i] = i + 1
					i += 1
					if(cnt + i == len(substring)):
						break
	return(pitable)

#ALGORITMA STRING MATCHING BOYERMOORE
def BM(substring, string):
	string = string.lower()
	substring = substring.lower()
	charcocok = 0
	tempcocok = 0
	i = len(substring) - 1
	j = len(substring) - 1

	if(len(substring) == 0 or len(string) == 0):
		return(0)

	while(i < len(string)):
		if(substring[j] == string[i]):
			if j == 0:
				return(len(substring)/len(string) * 100)
			else:
				charcocok += 1
				i -= 1
				j -= 1
		else:
			if(tempcocok < charcocok):
				tempcocok = charcocok
			LOtable = LastOccurence(substring[:j])
			l = findval(LOtable, string[i])
			i = i + len(substring) - min(j, 1+l)
			charcocok = 0
			j = len(substring) - 1
	return(tempcocok/len(string) * 100)

#fungsi last occurence buat booyer moore
def LastOccurence(substring):
	last = []
	temp = []
	for x in range(len(substring)):
		last.append([substring[x], substring.rfind(substring[x])])
	for x in last:
		if(x not in temp):
			temp.append(x)
	#print(temp)
	return(temp)

def findval(lotable, char):
	for x in lotable:
		if(x[0] == char):
			return(x[1])
	return(9999)


#ALGORITMA REGEX LITERALLY NGEMATCH DOANG
def regexmatch(substring, string):
	if(len(substring) == 0):
		return(0)
	matchlist = re.findall(substring, string)
	if(len(matchlist) == 0):
		return(0)
	else:
		floatret = len(matchlist[0])/len(string) * 100
		return(floatret)


#fungsi buat bikin testcase

def randomString(stringLength):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomSub(stringer):
	a = 0
	b = 0
	while(a == b):
		a = random.randint(0, len(stringer))
		b = random.randint(0, len(stringer))
	c = min(a,b)
	d = max(a,b)
	sublist = []
	subs = ''
	for x in range(c,d):
		sublist.append(stringer[x])
		subs = ''.join(sublist)	
	return(subs)




def main():
	
	#testcase ngegenerate random string dan substring yang udh pasti ada di dalem
	#semua tc harus return True
	print('\n\nTC SEMUA TRUE\n\n')
	for x in range(3,30):
		string = randomString(x)
		pattern = randomSub(string)
		print ('random string = ' + string)
		print ('random substring = ' + pattern)
	
		
		boolKMP = KMP(pattern, string)
		boolBM = BM(pattern, string)
		boolRegex = regexmatch(pattern, string)

		print('KMP \t', end = '')
		print(boolKMP)
		print('BM \t', end = '') 
		print(boolBM)
		print('Regex \t', end = '')
		print(boolRegex)


		#if(boolKMP != boolBM):
		#	print('TC WRONG ANSWER')
	
	#testcase ngegenerate random string dan substring yang udh pasti gk ada di dalem
	#semua tc harus return False
	print('\n\nTC SEMUA FALSE\n\n')

	for x in range(3,30):
		string = randomString(x)
		pattern = randomString(x)
		print ('random string = ' + string)
		print ('random substring = ' + pattern)
	
		boolKMP = KMP(pattern, string)
		boolBM = BM(pattern, string)
		boolRegex = regexmatch(pattern, string)

		print('KMP \t', end = '')
		print(boolKMP)
		print('BM \t', end = '') 
		print(boolBM)
		print('Regex \t', end = '')
		print(boolRegex)

		#if(boolKMP != boolBM):
		#	print('TC WRONG ANSWER')
	
	string = "Apakah chatbot itu manusia ?"
	pattern = "Apakah chatbot ?"
	print()
	#print(len(string))
	#print(len(pattern))
	print(KMP(pattern, string))
	print(BM(pattern, string))

