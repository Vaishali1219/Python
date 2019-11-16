def findIndex(c, d):
    res = {}
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i] == d[j]:
                if j not in res:
                    res[j] = d[j]
    return res

def findMaxSum(f):
    i = 0
    t = {}
    j = f.copy()
    for key in j:
        if key in f:
            cur = key
            prev = key - 1
            nxt = key + 1
            if f[cur] < 0:
                f.pop(cur)
            if prev in f:
                t[prev] = f[prev]
                f.pop(prev)
            if nxt in f:
                t[nxt] = f[nxt]
                f.pop(nxt)
    print(t)
    if sum(f.values()) == sum(t.values()):
        a = min(f.keys(), key = (lambda k: f[k]))
        b = min(t.keys(), key = (lambda k: t[k]))
        if f[a] > t[b]:
            return f
        else:
            return t
    else:
        return f

def getString(x):
    total = " "
    for p in range(0, len(x)):
        if x[p] > 0:
            total += str(x[p])
    return total

test = True
res_Lis = []
while test == True:
    T = int(input())
    if T > 0 and T < 11:
        test = False

for n in range(T):
    while test == False:
        N = int(input())
        if N > 0 and N <= 10000:
            test = True
            
    a = [int(x) for x in input().split() [:N]]

    for i in a:
        if i < -1000 and i > 1000:
            a[i] = 0
            
    if len(a) != N:
        for k in range(N - len(a)):
            a.append(0)
            
    b = a.copy()
    b.sort(reverse = True)
    index = findIndex(b, a)
    sumInd = findMaxSum(index)
    sumInd = sorted(sumInd.keys())
    d = []
    sumInd = findMaxSum(index)
    for key in sumInd:
        d.append(sumInd[key])
    finstr = getString(d)
    res_Lis.append(finstr)
    test = False

for i in range(len(res_Lis)):
    print(res_Lis[i].lstrip())
        
    

    

        
        
        
        
