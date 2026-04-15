# subset sums 

# Given an array arr of integers, return the sums of all subsets in the list.  Return the sums in any order

def subset_sums(i, a, arr, result):
    if i >= len(arr):
        result.append(a)
        return

    a += arr[i]
    subset_sums(i + 1, a, arr, result)
    a -= arr[i]
    subset_sums(i + 1, a, arr, result)


result = []
subset_sums(0, 0, [1, 2, 1], result)
print(result)

#TC :
#SC :


# subset sum II

#Given an integer array nums that may contain duplicates, return all possible subsets (the power set) ,The solution set must not contain duplicate subsets.

def subset_sum_II(i, a, arr, result):
    
    result.append(a.copy())

    for j in range(i, len(arr)):
        if j != i and arr[j] == arr[j - 1]:
            continue
        a.append(arr[j])
        print(j + 1, a)
        subset_sum_II(j + 1, a, arr, result)
        a.pop()


result = []
subset_sum_II(0, [], sorted(nums), result)
print(result)

#TC :
#SC :
