#swaping an array
def swap(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    swap(arr,l+1,r-1)


arr=[1,2,3,4,5]
swap(arr,l=0,r=len(arr)-1)
print(arr)
TC=O(N)  #N/2 AS we go till middle
SC=O(N)  #N/2 AS we go till middle

#palindrome check
def palindrome(arr,l,r):
    if l>=r:
        return True
    if arr[l]!=arr[r]:
        return False
    return palindrome(arr,l+1,r-1)

s="dummud"
print(palindrome(s,l=0,r=len(s)-1))
TC=O(N)  #N/2   AS we go till middle
SC=O(N)  #N/2   AS we go till middle
