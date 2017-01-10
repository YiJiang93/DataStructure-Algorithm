#258
def addDigits(self, num):
	"""
	:type num: int
	:rtype: int
	"""
	res=str(num)
	while len(res)>1:
		tmp=0
		for i in range(len(res)):
			tmp+=int(res[i])
		res=str(tmp)
	return int(res)
#172
def trailingZeroes(self, n):
	"""
	:type n: int
	:rtype: int
	"""
	if n==0:
		return 0
	else:
		return n/5+self.trailingZeroes(n/5)

#9
def isPalindrome(self, x):
	"""
	:type x: int
	:rtype: bool
	"""
	x=str(x)
	leng=len(x)
	if leng==1:
		return True
	if leng%2==0:
		return x[:leng/2]==x[leng/2:][::-1]
	if leng%2!=0:
		return x[:leng/2]==x[leng/2+1:][::-1]
		
#8
def myAtoi(self, str):
	"""
	:type str: str
	:rtype: int
	"""
	str = str.strip()
	str = re.findall('(^[\+\-0]*\d+)\D*', str)

	try:
		result = int(''.join(str))
		MAX_INT = 2147483647
		MIN_INT = -2147483648
		if result > MAX_INT > 0:
			return MAX_INT
		elif result < MIN_INT < 0:
			return MIN_INT
		else:
			return result
	except:
		return 0
		
#453
def minMoves(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	return sum(nums) - len(nums) * min(nums)

#13
def romanToInt(self, s):
	"""
	:type s: str
	:rtype: int
	"""
	roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
	z = 0
	for i in range(0, len(s) - 1):
		if roman[s[i]] < roman[s[i+1]]:
			z -= roman[s[i]]
		else:
			z += roman[s[i]]
	return z + roman[s[-1]]

#441
def arrangeCoins(self, n):
	"""
	:type n: int
	:rtype: int
	"""
	i=1
	while n-i>=0:
		n=n-i
		i+=1
	return i-1
	
#326
def isPowerOfThree(self, n):
	"""
	:type n: int
	:rtype: bool
	"""
	return n>0 and 3**19%n==0
	
#223
def computeArea(self, A, B, C, D, E, F, G, H):
	"""
	:type A: int
	:type B: int
	:type C: int
	:type D: int
	:type E: int
	:type F: int
	:type G: int
	:type H: int
	:rtype: int
	"""
	total=(G-E)*(H-F)+(C-A)*(D-B)
	overlap= max(min(C,G)-max(A,E), 0)*max(min(D,H)-max(B,F), 0)
	return total-overlap
	
#202
def isHappy(self, n):
	"""
	:type n: int
	:rtype: bool
	"""
	nums=[]
	while n!=1:
		n = sum([int(i) ** 2 for i in str(n)])
		if n in nums:
			return False
		else:
			nums.append(n)
	return True
	
#7
def reverse(self, x):
	"""
	:type x: int
	:rtype: int
	"""
	if x >0:
		x=str(x)[::-1]
		x=int(x)
	if x<0:
		x=str(x)[1:]
		x=x[::-1]
		x=0-int(x)
	if abs(x)>0x7FFFFFFF:
		return 0
	return x
	
#168
def convertToTitle(self, n):
	"""
	:type n: int
	:rtype: str
	"""
	chapters=[chr(x) for x in range(ord("A"),ord("Z")+1)]
	result=[]
	while n >0:
		result.append(chapters[(n-1)%26])
		n=(n-1)//26
	result.reverse()
	return "".join(result)
	
#171
def titleToNumber(self, s):
	"""
	:type s: str
	:rtype: int
	"""
	s=s[::-1]
	sum1=0
	for k,v in enumerate(s):
		sum1+=(ord(v)-64)*(26**k)
	return sum1

#263
def isUgly(self, num):
	"""
	:type num: int
	:rtype: bool
	"""
	dic=[2,3,5]
	for e in dic:
		while num%e==0 and num%e<num:
			num=num/e
	return num==1

#67
def addBinary(self, a, b):
	"""
	:type a: str
	:type b: str
	:rtype: str
	"""
	return bin(int(a,2)+int(b,2))[2:]
	
#66
def plusOne(self, digits):
	"""
	:type digits: List[int]
	:rtype: List[int]
	"""
	ind=-1
	digits[-1]=digits[-1]+1
	while ind>=-len(digits):
		if digits[ind]>9:
			digits[ind]-=10
			if ind-1<-len(digits):
				digits.insert(0,0)
			digits[ind-1]+=1
		ind-=1
	return digits

#204
def countPrimes(self, n):
	"""
	:type n: int
	:rtype: int
	"""
	if n<=2:
		return 0
	prime=[True]*n
	prime[:2] = [False, False]
	for i in range(2, int(n ** 0.5) + 1):
		if prime[i]:
			prime[i*i:n:i]=[False]*len(prime[i*i:n:i])
	return sum(prime)

#396	
def maxRotateFunction(self, A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	if len(A)==0:
		return 0
	totalSum=sum(A)
	Local_Max=0
	for i in range(len(A)):
		Local_Max+=i*A[i]
	Global_Max=Local_Max
	for i in range(len(A)-1,0,-1):
		Local_Max+=(totalSum-A[i]*len(A))
		Global_Max=max(Local_Max,Global_Max)
	return Global_Max