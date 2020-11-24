def solution(nums):
    cards = [0] * 10
    for n in nums:
        cards[n] += 1

    counts = 0
    print(cards)
    for i in range(1, 10):
        if cards[i] == 0:
            continue
        
        j = i
        found = True
        while j < i + 3:
            if cards[j] != 0:
                cards[j] -= 1
                j += 1
            else:
                found = False
                break

        if found:
            counts += 1
    return counts == 4

def solution2(nums):
    cards = [0] * 10
    for n in nums:
        cards[n] += 1

    for i in range(1, 10):
        if cards[i] == 0:
            continue
        count = cards[i]
        for j in range(i, i+4):
            cards[j] -= count
            if cards[j] < 0:
                return False
    return True
print(solution([ 1, 4, 3, 2, 5, 7, 8, 6, 9, 3, 2, 4]))
print(solution2([ 1, 4, 3, 2, 5, 7, 8, 6, 9, 3, 2, 4]))
