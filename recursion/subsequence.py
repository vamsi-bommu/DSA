# Print all subsequences

def subsequence(n,a,arr):
    if n>=len(arr):
        print(a)
        return

    a.append(arr[n])
    subsequence(n+1,a,arr) #take 
    a.pop()
    subsequence(n+1,a,arr) #not take
    
subsequence(0,[],arr=[3,1,2,7])

#print subsequences whose sum is k

def subseq(i,a,arr,sum,s):

    if i>=len(arr):
        if sum==s:
            print(a)
        return

    a.append(arr[i])
    subseq(i+1,a,arr,sum+arr[i],s)
    a.pop()
    subseq(i+1,a,arr,sum,s)

subseq(0,[],[1,2,1,1],0,2)

