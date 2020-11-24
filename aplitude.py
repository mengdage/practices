def solution(nums):
    nums = sorted(nums)
    
    minAmplitude = float('inf')
    for i in range(len(nums) - 2):
        j = i + (len(nums) - 3) - 1
        minAmplitude = min(nums[j] - nums[i], minAmplitude)
    
    return minAmplitude

print(solution([-1, 3, -1, 8, 5, 4]))
print(solution([10, 10, 3, 4, 10]))
