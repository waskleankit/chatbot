def pattern(n): #5
    k = n-1 #4
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1 #3 #2
        for j in range(0,i+1): #1
            print("*",end=" ")
        print("\r")

n =5
pattern(n)