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


# #Nth fibonacci 
m,n=0,1
N=7
for i in range(N-2):
    t=m+n
    m=n
    n=t

print(n)
TC=O(N)
SC=O(1)

#Nth fibonacci using recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(8))
TC=O(2**N)  #each call makes 2 recursive calls
SC=O(N)     #
