def singleNumber(nums):
    result = 0
    
    for num in nums:
        result ^= num
    
    return result

print(singleNumber([2, 2, 1]))    
print(singleNumber([4, 1, 2, 1, 2]))  
print(singleNumber([1]))