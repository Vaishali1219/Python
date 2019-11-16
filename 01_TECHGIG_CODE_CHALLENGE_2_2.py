def main():
    res_Lis = []
    T = int(input())
            
    for n in range(T):
        N = int(input())
        
        a = [int(x) for x in input().split() [:N]]
        b = a.copy()
        b.sort(reverse = True)
        index = {}
        index = {j : b[i] for i in range(len(b)) for j in range(len(b)) if b[i] == a[j] if j not in index}
        f = index.copy()
        t = {}
        for key in f:
            if key in index:
                cur = key
                prev = key - 1
                nxt = key + 1
                if index[cur] < 0:
                    index.pop(cur)
                if prev in index:
                    t[prev] = index[prev]
                    index.pop(prev)
                if nxt in index:
                    t[nxt] = index[nxt]
                    index.pop(nxt)
        
        if sum(index.values()) == sum(t.values()):
            a = min(index.keys(), key = (lambda k: index[k]))
            b = min(t.keys(), key = (lambda k: t[k]))
            if index[a] > t[b]:
                sumInd = index.copy()
            else:
                sumInd = t.copy()
        else:
            sumInd = index.copy()


        d = [sumInd[key] for key in sorted(sumInd.keys())]
        total = " "
        for p in range((len(d) - 1), -1, -1):
            if d[p] > 0:
                total += str(d[p])
        res_Lis.append(total)
        
    for i in range(len(res_Lis)):
        print(res_Lis[i].lstrip())

 # Write code here 

main()
