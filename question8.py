def minDifference(nums, k):
    if len(nums) <= 4:
        return 0
    
    nums.sort()
    min_num = float('inf')
    max_num = float('-inf')
    
    for i in range(len(nums)):
        if i >= k and len(nums) - i > k:
            min_num = min(min_num, nums[i] - k)
            max_num = max(max_num, nums[i] + k)
    
    return max_num - min_num


nums = [1]
k = 0
print(minDifference(nums, k))  
