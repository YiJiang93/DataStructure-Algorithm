#463
def islandPerimeter(self, grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	s=0
	for row in grid:
		s+=sum(map(operator.ne,[0]+row,row+[0]))
	for row in map(list,zip(*grid)):
		s+=sum(map(operator.ne,[0]+row,row+[0]))
	return s

#447
def numberOfBoomerangs(self, points):
	"""
	:type points: List[List[int]]
	:rtype: int
	"""
	res=0
	for p in points:
		dic={}
		for q in points:
			x=p[0]-q[0]
			y=p[1]-q[1]
			dic[x**2+y**2]=1+dic.get(x**2+y**2,0)
		for k in dic:
			res+=dic[k]*(dic[k]-1)
	return res
	
#438
def findAnagrams(self, s, p):
	"""
	:type s: str
	:type p: str
	:rtype: List[int]
	"""
	res=[]
	pCounter=Counter(p)
	sCounter=Counter(s[:len(p)-1])
	for i in range(len(p)-1,len(s)):
		sCounter[s[i]]+=1
		if sCounter==pCounter:
			res.append(i-len(p)+1)
		sCounter[s[i-len(p)+1]]-=1
		if sCounter[s[i-len(p)+1]]==0:
			del sCounter[s[i-len(p)+1]]
	return res
	
#409
def longestPalindrome(self, s):
	"""
	:type s: str
	:rtype: int
	"""
	dic={}
	res=0
	for e in s:
		dic[e]=dic.get(e,0)+1
	for k,v in dic.items():
		res+=v-v%2
	return res+1 if res<len(s) else res 
	
#389
def findTheDifference(self, s, t):
	"""
	:type s: str
	:type t: str
	:rtype: str
	"""
	dic1={}
	dic2={}
	for e in s:
		dic1[e]=dic1.get(e,0)+1
	for e in t:
		dic2[e]=dic2.get(e,0)+1
	for k, v in dic2.items():
		if k not in dic1:
			return k
		if k in dic1:
			if v!=dic1[k]:
				return k
			
#350
def intersect(self, nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	dic={}
	res=[]
	for e in nums1:
		dic[e]=dic.get(e,0)+1
	for num in nums2:
		if num in dic and dic[num]>0:
			res.append(num)
			dic[num]-=1
	return res
	
#349
def intersection(self, nums1, nums2):
	"""
	:type nums1: List[int]
	:type nums2: List[int]
	:rtype: List[int]
	"""
	res=[]
	nums1=set(nums1)
	nums2=set(nums2)
	for e in nums1:
		if e in nums2:
			res.append(e)
	return res
	
#299
def getHint(self, secret, guess):
	"""
	:type secret: str
	:type guess: str
	:rtype: str
	"""

	bull=0
	sec=map(int,secret)
	gue=map(int,guess)
	sec1=[0]*10
	gue1=[0]*10
	for i in range(len(secret)):
		if sec[i]==gue[i]:
			bull+=1
		else:
			sec1[sec[i]]+=1
			gue1[gue[i]]+=1
	cow=sum(map(min,zip(sec1,gue1)))
	return "%dA%dB"%(bull,cow)