#print from 1 to N (Functional)
def f(i,n):
    if i>n:
        return
    print(i,end=" ")
    f(i+1,n)
    
#f(1,N)

#print from 1 to N (Backtracking)
def f(i,n):
    if i<1:
        return
    f(i-1,n)
    print(i,end=" ")
    

#f(N,N)


#print from N to 1 
def f(i,n):
    if i<1:
        return
    print(i,end=" ")
    f(i-1,n)

#f(N,N)


#print from N to 1 (Backtracking)
def f(i,n):
    if i>n:
        return
    f(i+1,n)
    print(i,end=" ")
    
#f(1,N)

   

