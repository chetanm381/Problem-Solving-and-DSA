from queue import Empty


def match(ps):
    ps=list(ps)
    stack=[]
    dictt={"{":"}","(":")","[":"]"}
    for x in ps:
        val=dictt.get(x)
        if val :
            stack.append(x)
        else :
            try:
                t=stack.pop()
                if(dictt.get(t)!=x):
                    return False    
            except:
                return False           
    if(len(stack)==0):
        return True
    else:
        return False    

def biggestBracket(ps):
    ps=list(ps)
    stack=[]
    bracket=[]
    check=0
    checktemp=[]
    dictt={"{":"}","(":")","[":"]"}
    for x in ps:
        if len(stack)==0:
            if (check<len(bracket)):
                checktemp=bracket
                bracket=[]
        val=dictt.get(x)
        if val is None:
            try:
                stack.pop()   
                bracket.append(x)
            except:
                pass
        else :
            stack.append(x)
            bracket.append(x)
    if len(checktemp)==0:
        checktemp=bracket        
    return ''.join(checktemp)       





        
        



    


if __name__ == '__main__':
    testCases = ["{{}}", "{{{}}", "{{{{}}}","{{{}{}}}",  "}{","([][{({}){}}])",")[{({}){}}]())","([{})]","{[]}()]()"]
    results =   ["{{}}", False, False,"{{{}{}}}",  False,"([][{({}){}}])",False,False,False]
    for i in range(len(testCases)):
        if match(testCases[i]) == True:
            if biggestBracket(testCases[i]) == results[i]:
                print("Test Succeed ",i)
            else:
                print("Test Failed ", i)
        else :
            print("Given string is not valid in Test Case",i)        