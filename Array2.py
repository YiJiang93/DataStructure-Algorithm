#64
def minPathSum(self, grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	m=len(grid)
	n=len(grid[0])
	for i in range(1,n):
		grid[0][i]+=grid[0][i-1]
	for j in range(1,m):
		grid[j][0]+=grid[j-1][0]
	for j in range(1,m):
		for i in range(1,n):
			grid[j][i]+=min(grid[j][i-1],grid[j-1][i])
	return grid[-1][-1]
	
#167
def twoSum(self, numbers, target):
	"""
	:type numbers: List[int]
	:type target: int
	:rtype: List[int]
	"""
	dic={}
	for i in range(len(numbers)):
		if numbers[i] in dic:
		   return [dic[numbers[i]]+1,i+1]
		if numbers[i] not in dic:
			dic[target-numbers[i]]=i
	return None

#162
def findPeakElement(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	if len(nums)<=2:
		return nums.index(max(nums))
	for i in range(1,len(nums)-1):
		if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
			return i
	if nums[0]>nums[1]:
		return 0
	if nums[-1]>nums[-2]:
		return len(nums)-1

#209
def minSubArrayLen(self, s, nums):
	"""
	:type s: int
	:type nums: List[int]
	:rtype: int
	"""
	left,result=0,0
	leng=len(nums)+1
	for right,n in enumerate(nums):
		result+=n
		while result>=s:
			leng=min(leng,right-left+1)
			result=result-nums[left]
			left+=1
	return leng if leng<=len(nums) else 0
	
#153
def findMin(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	i = 0
	j = len(nums) - 1
	while i < j:
		m = i + (j - i) / 2
		if nums[m] > nums[j]:
			i = m + 1
		else:
			j = m
	return nums[i]
	
def findMin(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	low=0
	high=len(nums)-1
	if len(nums)==1:
		return nums[0]
	while low<=high:
		mid=(low+high)//2
		if mid==0:
			return nums[mid+1] if nums[mid+1]<nums[mid] else nums[mid]
		if mid==len(nums)-1:
			return nums[mid] if nums[mid]<nums[mid-1] else nums[mid-1]
		if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
			return nums[mid]
		if nums[mid]>nums[mid-1] and nums[mid]>nums[high]:
			low=mid+1
		if nums[mid]>nums[mid-1] and nums[mid]<nums[high]:
			high=mid-1