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


#print only one subsequence whose sum is k

def singlesubseq(i,a,arr,sum,s):
    if i>=len(arr):
        if s==sum:
            print(a)
            return True
        return False

    a.append(arr[i])
    s+=arr[i]
    if singlesubseq(i+1,a,arr,sum,s):
        return True
    a.pop()
    s-=arr[i]
    if singlesubseq(i+1,a,arr,sum,s):
        return True

    #if we don't have any sequence and we ran out of entire array
    return False

singlesubseq(0,[],[1,21,11,11],2,0)


#print the count of all subsequences which has sum k

def countsubseq(i,s,sum,arr,c):
    if i>=len(arr):
        if s==sum:
             c+=1
        return c
    
    s+=arr[i]
    c=countsubseq(i+1,s,sum,arr,c)

    s-=arr[i]
    c=countsubseq(i+1,s,sum,arr,c)
    return c
    
    #alternative way (standard way)
    #if i>=len(arr):
    #    if sum==s:
    #     return 1
    # return 0
    #l=countsubseq(i+1,s+arr[i],sum,arr) #no need to carry a variable c
    #r=countsubseq(i+1,s,sum,arr)
    #return l+r

print(countsubseq(0,0,2,[1,2,1,1],0))    