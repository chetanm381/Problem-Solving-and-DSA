def BlackJack(A,B):
    Number_to_Win=21-(A+B)
    if(1<=Number_to_Win<=10):
        print(Number_to_Win)
    else:
        print("-1")    


if __name__=="__main__":
    try : 
        t=int(input())
        for i in range(t):
            A,B=map(int,input().split(" "))
            BlackJack(A,B)
    except:
        pass
    
