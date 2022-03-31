import numpy as np

def countCoinsPossibility(A):
    cols=A[0]+1
    coins=A[1]
    rows=len(coins)
    coins.sort()
    a = np.zeros([rows,cols],int)
    for i in range(rows):
        a[i][0]=1
        for j in range(1,cols):
            if(i==0):
                if(coins[i]<=j):
                    a[i][j]=a[i][j-coins[i]]
                else:
                    a[i][j]=0
            else:
                if(coins[i]<=j):
                    a[i][j]=a[i-1][j]+a[i][j-coins[i]]
                else:
                    a[i][j]=a[i-1][j] 
    print(a)                   
    return a[rows-1][cols-1]


if __name__=="__main__":
    testcase=[[5,[1,2,3]],[15,[2,3,5,10]]]
    result=[5,9]
    for i in range(0,len(testcase)):
        if countCoinsPossibility(testcase[i])==result[i]:
            print("Test Case Passed")
        else:
            print("Test Case Failed")    