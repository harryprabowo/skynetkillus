import random
import string
import re

#Algoritma KMP, inputnya substring sama string, return boolean
def KMP(substring, string):
	result = False
	pitable = []
	newpitable = []
	newpitable = [0]
	subsList = ['x']
	stringList = ['x']
	pitable = KMPspindex(substring)
	
	for x in pitable:
		newpitable.append(x)
	for x in substring:
		subsList.append(x)
	for x in string:
		stringList.append(x)
	
	if(len(substring) == 0):
		return(True)

	matchindex = -1
	i = 1
	j = 0
	while(i < len(stringList)):
		if(subsList[j+1] == stringList[i]):
			j += 1
			i += 1
		else:
			if(j == 0):
				i += 1
			else:
				j = newpitable[j]

		#compare success
		if(j + 1 == len(subsList)):
			result = True
			matchindex = i - len(substring)
			break
	return(result)


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
	LOtable = LastOccurence(substring)
	i = len(substring) - 1
	j = len(substring) - 1

	if(len(substring) == 0):
		return(True)

	while(i < len(string)):
		if(substring[j] == string[i]):
			if j == 0:
				return(True)
			else:
				i -= 1
				j -= 1
		else:
			l = findval(LOtable, string[i])
			i = i + len(substring) - min(j, 1+l)
			j = len(substring) - 1 
	return(False)

#fungsi last occurence buat booyer moore
def LastOccurence(substring):
	last = []
	temp = []
	for x in range(len(substring)):
		last.append([substring[x], substring.rfind(substring[x])])
	for x in last:
		if(x not in temp):
			temp.append(x)
	return(temp)

def findval(lotable, char):
	for x in lotable:
		if(x[0] == char):
			return(x[1])
	return(-1)


#ALGORITMA REGEX LITERALLY NGEMATCH DOANG
def regexmatch(substring, string):
	if(len(substring) == 0):
		return(True)
	matchlist = re.findall(substring, string)
	if(len(matchlist) == 0):
		return(False)
	else:
		return(True)


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


		if(boolKMP != boolBM):
			print('TC WRONG ANSWER')
	
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


		if(boolKMP != boolBM):
			print('TC WRONG ANSWER')
	
main()