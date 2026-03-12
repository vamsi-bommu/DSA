## Print all subsequences

def subsequence(n,a,arr):
    if n>=len(arr):
        print(a)
        return

    a.append(arr[n])
    subsequence(n+1,a,arr) #take 
    a.pop()
    subsequence(n+1,a,arr) #not take
    
subsequence(0,[],arr=[3,1,2,7])

