def twoSum(nums, target):
    hash_map = {}  # Stores {number: index}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return []  # Should not be reached given the problem constraints
    
if __name__=="__main__":
    nums = [2,7,11,15, 6, 3]
    target = 9
    print(twoSum(nums, target))