# Print all subsequences


def subsequence(n, a, arr):
    if n >= len(arr):
        print(a)
        return

    a.append(arr[n])
    subsequence(n + 1, a, arr)  # take
    a.pop()
    subsequence(n + 1, a, arr)  # not take


subsequence(0, [], arr=[3, 1, 2, 7])


# print subsequences whose sum is k


def subseq(i, a, arr, sum, s):

    if i >= len(arr):
        if sum == s:
            print(a)
        return

    a.append(arr[i])
    subseq(i + 1, a, arr, sum + arr[i], s)
    a.pop()
    subseq(i + 1, a, arr, sum, s)


subseq(0, [], [1, 2, 1, 1], 0, 2)


# print only one subsequence whose sum is k


def singlesubseq(i, a, arr, sum, s):
    if i >= len(arr):
        if s == sum:
            print(a)
            return True
        return False

    a.append(arr[i])
    s += arr[i]
    if singlesubseq(i + 1, a, arr, sum, s):
        return True
    a.pop()
    s -= arr[i]
    if singlesubseq(i + 1, a, arr, sum, s):
        return True

    # if we don't have any sequence and we ran out of entire array
    return False


singlesubseq(0, [], [1, 21, 11, 11], 2, 0)


# print the count of all subsequences which has sum k


def countsubseq(i, s, sum, arr, c):
    if i >= len(arr):
        if s == sum:
            c += 1
        return c

    s += arr[i]
    c = countsubseq(i + 1, s, sum, arr, c)

    s -= arr[i]
    c = countsubseq(i + 1, s, sum, arr, c)
    return c

    # alternative way (standard way)
    # if i>=len(arr):
    #    if sum==s:
    #     return 1
    # return 0
    # l=countsubseq(i+1,s+arr[i],sum,arr) #no need to carry a variable c
    # r=countsubseq(i+1,s,sum,arr)
    # return l+r


print(countsubseq(0, 0, 2, [1, 2, 1, 1], 0))


# print all combinations whose sum is equal to target
# combination sum 1


def combinationSum(i, a, arr, target, result):
    if i >= len(arr):
        if sum(a) == target:
            result.append(a.copy())

        return

    if sum(a) + arr[i] <= target:
        a.append(arr[i])
        combinationSum(i, a, arr, target, result)
        a.pop()

    combinationSum(i + 1, a, arr, target, result)


result = []
print(combinationSum(0, [], [2, 3, 5, 7], 7, result))
print(result)

# TC: O((2^t)*k)   ---> k is the avg time taken to put 'a' into the result list,for an index 2 options will be there but it can be any no.of times we take the same element
# SC: O(k*x)   ---> k is the avg size of the list 'a' and x is the number of such lists {here we don't take auxilary stack space because it is unpredictable}


# combination sum 2 (brute force)


def combinationSum2(i, a, arr, target, result):
    if sum(a) > target:
        return

    if i >= len(arr):
        if sum(a) == target and sorted(a) not in result:
            result.append(sorted(a.copy()))

        return

    a.append(arr[i])
    combinationSum2(i + 1, a, arr, target, result)
    a.pop()
    combinationSum2(i + 1, a, arr, target, result)


ans = []
combinationSum2(0, [], [2, 5, 2, 1, 2], 5, ans)
print(ans)


# combination sum 2 (optimized)


def combinationSum2o(i, a, arr, target, result):

    if target == 0:
        result.append(a[:])
        return

    for j in range(i, len(arr)):
        if j != i and arr[j - 1] == arr[j]:
            continue

        if arr[j] > target:
            break
        a.append(arr[j])
        combinationSum2o(j + 1, a, arr, target - arr[j], result)
        a.pop()


result = []
combinationSum2o(0, [], sorted([1, 1, 1, 2, 2]), 4, result)
print(result)

# TC:O((2**n)*k  k=Avg length of a
# SC: O(n*k*x)   x=no.of combinations