if __name__=="__main__":
    try : 
        t=int(input())
        for i in range(t):
            A=int(input())
            if A%10==0:
                print(A//10)
            else:
                print((A//10)+1)    

    except:
        pass
    
