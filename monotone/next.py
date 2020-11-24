def next_smaller(nums):
    ns = [-1] * len(nums)

    stack = []
    stack.append(len(nums) - 1)

    for i in range(len(nums) - 2, -1, -1):
        # pop invalid indexes
        while stack and nums[stack[-1]] > nums[i]:
            stack.pop()

        # check if a vlaid index exists
        if stack and nums[stack[-1]] < nums[i]:
            ns[i] = stack[-1]

        # the current index is always a candidate
        stack.append(i)
    
    return ns
def next_greater(nums):
    l = len(nums)
    ng = [-1] * l

    stack = []
    stack.append(l-1)
    for i in range(l-2, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack and nums[stack[-1]] > nums[i]:
            ng[i] = stack[-1]
        stack.append(i)
    return ng

if __name__ == '__main__':
    n1 = [4, 8, 5, 7, 3, 2]
    n2 = [91, 10, 3, 22, 40]
    print(next_smaller(n1))
    print(next_greater(n2))
