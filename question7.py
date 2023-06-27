def isMonotonic(nums):
    isIncreasing = False
    isDecreasing = False

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            isIncreasing = True
        elif nums[i] < nums[i - 1]:
            isDecreasing = True

        if isIncreasing and isDecreasing:
            return False

    return True


nums = [1, 2, 2, 3]
print(isMonotonic(nums))  
