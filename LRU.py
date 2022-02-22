import random


def n_recent_nums(newNum, lastNNums):

    return newNum

if __name__ == '__main__':
    random.seed(7)
    nums = 20
    n = 5
    t=[]
    for num in range(nums):
        recentNums = n_recent_nums(int(random.random()*1000), n)
        print(recentNums)
        if(num<5):
             t.append(recentNums)
        else:

            try:
                t.remove(recentNums)
            except:
                t.remove(t[0])

            t.append(recentNums)
                     
    print(t)