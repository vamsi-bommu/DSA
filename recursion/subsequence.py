arr=[3,1,2,7]

def subsequence(n,a):
    if n>=len(arr):
        print(a)
        return
    
    a.append(arr[n])
    subsequence(n+1,a)
    a.pop()
    subsequence(n+1,a)
    

subsequence(0,[])