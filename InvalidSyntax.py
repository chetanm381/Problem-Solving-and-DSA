def match(ps):
    ps = list(ps)
    # you are using this list as stack so name it stack instead of temp
    stack = []
    dictt = {"{": "}", "(": ")", "[": "]"}
    for x in ps:
        # you are using dict as list instead of that you can get the value from dict
        # if it comes nil that means key does not exist in the map
        val = dictt.get(x)
        if val is None:
            if val != x:
                return False
            else:
                stack.pop()
        else:
            stack.append(x)
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    testCases = ["{{}}", "{{{}}", "{{{{}}}","{{{}{}}}",  "}{","([][{({}){}}])",")[{({}){}}]())","([{})]"]
    results =   [True  ,   False,     False,      True, False,             True,           False,   False]
    for i in range(len(testCases)):
        if match(testCases[i]) == results[i]:
            print("Test Succeed ",i)
        else:
            print("Test Failed ", i)
