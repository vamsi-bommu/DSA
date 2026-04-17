# Given an array nums of distinct integers, return all the possible permutations.

# permutations I (brute force)


def permute(a, map, arr, result, x):
    if len(a) == x:
        result.append(a.copy())
        return

    for i in range(len(arr)):
        if map[i] != 1:
            a.append(arr[i])
            map[i] = 1
            permute(a, map, arr, result, x)
            a.pop()
            map[i] = 0


nums = [1, 2, 3]
result = []
permute([], [0] * len(nums), nums, result, len(nums))
print(result)

# TC : O(N*N!)  #N for copying the array
# SC : O(N+N+N+N!)     # N for a, N for map, N for stack space and N! for the result


# permutations I (optimized)


def perm(i, arr, result):
    if i >= len(arr):
        result.append(arr[:])
        return
    for j in range(i, len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        perm(
            i + 1, arr, result
        )  # here we fix the position of j at i then we start at i+1 for next iteration
        arr[i], arr[j] = arr[j], arr[i]


r = []
perm(0, [1, 2, 3], r)
print(r)


# TC : O(N*N!)  #N for putting the array in result
# SC : O(N+N!)     # N for stack space and N! for the result
