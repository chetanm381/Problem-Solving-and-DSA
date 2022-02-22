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


if __name__ == '__main__':
    testCases = ["{{}}", "{{{}}", "{{{{}}}","{{{}{}}}",  "}{","([][{({}){}}])",")[{({}){}}]())","([{})]","{[]}()]()"]
    results =   [True  ,   False,     False,      True, False,             True,           False,   False,   False]
    for i in range(len(testCases)):
        if match(testCases[i]) == results[i]:
            print("Test Succeed ",i)
        else:
            print("Test Failed ", i)