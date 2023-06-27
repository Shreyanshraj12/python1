def findLHS(nums):
    num_count = {}
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    max_length = 0
    for num in num_count:
        if num + 1 in num_count:
            length = num_count[num] + num_count[num + 1]
            if length > max_length:
                max_length = length

    return max_length


nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums))  
