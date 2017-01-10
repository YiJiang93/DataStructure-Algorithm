 #414
 def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [float('-inf')] * 3
        for n in nums:
            if n>l[0] and n not in l:
                heapq.heappushpop(l,n)
        return l[0] if l[0]!=float("-inf")else max(l)

#1
def twoSum(self, nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	if len(nums)<=1:
		return False
	dic={}
	for i in range(len(nums)):
		if nums[i] in dic:
			return [dic[nums[i]],i]
		if nums[i] not in dic:
			dic[target-nums[i]]=i
		
#448
def findDisappearedNumbers(self, nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	return list(set(range(1,len(nums)+1))-set(nums))
	
#283
def moveZeroes(self, nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	for e in nums:
		if e==0:
			nums.remove(e)
			nums.append(0)
			
#219
def containsNearbyDuplicate(self, nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: bool
	"""
	dic={}
	for i in range(len(nums)):
		if nums[i] in dic:
			if abs(dic[nums[i]]-i)<=k:
				return True
			else:
				dic[nums[i]]=i
		if nums[i] not in dic:
			dic[nums[i]]=i
	return False
	
#217
def containsDuplicate(self, nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	return len(set(nums))!=len(nums)
	
#189
def rotate(self, nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	k = k % (len(nums))
	nums[:]=nums[-k:]+nums[:-k]

#169
def majorityElement(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	return sorted(nums)[len(nums)/2]

#121
def maxProfit(self, prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	if prices==[]:
		return 0
	buy=prices[0]
	profit=0
	for i in range(1,len(prices)):
		if prices[i]<buy:
			buy=prices[i]
		lpro=prices[i]-buy
		profit=max(profit,lpro)
	return profit

#118 and 119
def generate(self, numRows):
	"""
	:type numRows: int
	:rtype: List[List[int]]
	"""
	res=[]
	for i in range(numRows):
		res.append([1]*(i+1))
		if i>1:
			for j in range(1,i):
				res[i][j]=res[i-1][j-1]+res[i-1][j]
	return res
	
#88
def merge(self, nums1, m, nums2, n):
	"""
	:type nums1: List[int]
	:type m: int
	:type nums2: List[int]
	:type n: int
	:rtype: void Do not return anything, modify nums1 in-place instead.
	"""

	while m>0 and n>0:
		if nums1[m-1]<nums2[n-1]:
			nums1[m+n-1]=nums2[n-1]
			n-=1
		else:
			nums1[m+n-1]=nums1[m-1]
			m-=1
	if n>0:
		nums1[:n]=nums2[:n]
		
#27
def removeElement(self, nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""
	for x in nums[:]:
		if x == val:
			nums.remove(val)
	return len(nums)
	
#26
def removeDuplicates(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if nums==[]:
		return 0
	tail=0
	for i in range(1,len(nums)):
		if nums[i]!=nums[tail]:
			tail+=1
			nums[tail]=nums[i]
	return tail+1