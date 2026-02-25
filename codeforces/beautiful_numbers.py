def result():
    #parse
    t = int(input())
    r = []
    for _ in range(t):
        a = input()
        # l = a.split()
        # n, m, d = (int(i) for i in l)
        r.append(test_min(a))
    for item in r:
        print(item)

def test_min(a):
    count = 0
    l1 = [int(i) for i in a]
    sum1 = sum(l1)
    l2 = [int(i) for i in str(sum1)]
    sum2 = sum(l2)
    # print(sum1)
    # print(sum2)
    if sum1>100:
        i = -1
        while(sum1 > 20):
            l1[i] = 0
            i -= 1
            count += 1
            sum1 = sum(l1)
    
    else:
        i = -1
        while(sum1 > 20):
            l1[i] = 0
            i -= 1
            count += 1
            sum1 = sum(l1)

    return count + 1




if __name__ == "__main__":
    result()
    #print(18*9)
