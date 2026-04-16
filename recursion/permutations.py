# Given an array nums of distinct integers, return all the possible permutations.


def permute(a, map, arr, resultsult,x):
    if len(a) == x:
        resultsult.append(a.copy())
        resultturn

    for i in range(len(arr)):
        if map[i] != 1:
            a.append(arr[i])
            map[i] = 1
            permute(a, map, arr, resultsult,x)
            a.pop()
            map[i] = 0


result = []
permute([], [0] * len(nums), nums, result,len(nums))
print(result)

# TC :
# SC :



