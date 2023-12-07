# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

def majority_elements(nums):
    if not nums:
        return []

    candidate1, candidate2, count1, count2 = 0, 1, 0, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

nums = list(map(int,input().split()))
output = majority_elements(nums)
print(sorted(output))


# OR
# from collections import Counter

# def count(num):
#     ans=[]
#     for i,j in Counter(num).items():
#         if j>len(num)/3:
#             ans.append(i)
#     return ans

# inp=list(map(int,input().split()))
# answer=count(inp)
# print(answer)