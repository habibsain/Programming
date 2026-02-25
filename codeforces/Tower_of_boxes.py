def result():
    #parse
    t = int(input())
    r = []
    for _ in range(t):
        a = input()
        l = a.split()
        n, m, d = (int(i) for i in l)
        r.append(test_min(n, m, d))
    for item in r:
        print(item)

def test_min(n, m, d):
    #min = 0
    factor = int(d/m)
    if factor == 0:
        min = n
    else:
        min = int(n/factor) - 1 if n%factor == 0 else int(n/factor) + 1
    return min

def test():
    #x = int(input("number:"))
    # for _ in range(x):
    #     a = input("list")
    #     l = a.split()
    #     print("type of x: "+ str(type(x)))
    #     print("type of a: "+ str(type(a)))
    # t = "2 5 6"
    # x = t.split()
    # a, b, c = (i for i in x)
    # print(f"{x}\n{a}\n{b}\n{c}")
    print(int(5/2))

if __name__ == "__main__":
    #test()
    result()