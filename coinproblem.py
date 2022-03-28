def countCoins(A):
    Amount=A[0]
    Coins=A[1]
    x=len(Coins)-1
    while(x>=0):
        temp=Coins[x]
        Coins[x]=Amount//temp
        Amount=Amount%temp
        x=x-1 
    return Coins

if __name__=="__main__":
    testcase=[[10,[1,3,5]],[12,[1,3,5,10]]]
    result=[[0,0,2],[2,0,0,1]]
    for i in range(0,len(testcase)):
        if countCoins(testcase[i])==result[i]:
            print("Test Case Passed")
        else:
            print("Test Case Failed")    