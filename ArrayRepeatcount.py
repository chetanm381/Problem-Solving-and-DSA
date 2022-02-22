def ArrayRepeatcount(a):
    Difference=len(a)
    Index=None
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                x=i
                y=j
                break
        temp=abs(x-y)
        if(Difference>temp):
            Index=x
            Difference=temp       
    return a[x]       
                


if __name__=="__main__":
    testCases=[[1,2,3,4,1],[1,2,3,4,3,1]]
    result=[1,3]
    for i in range(len(testCases)):
        if ArrayRepeatcount(testCases[i]) == result[i]:
            print("Test Succeed ",i)
        else:
            print("Test Failed ", i)