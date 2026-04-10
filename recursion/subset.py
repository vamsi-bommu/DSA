# subset sums
# Given an array arr of integers, return the sums of all subsets in the list.  Return the sums in any order


def comb(i, a, arr, result):
    if i >= len(arr):
        result.append(a)
        return

    a += arr[i]
    comb(i + 1, a, arr, result)
    a -= arr[i]
    comb(i + 1, a, arr, result)


result = []
comb(0, 0, [1, 2, 1], result)
print(result)
