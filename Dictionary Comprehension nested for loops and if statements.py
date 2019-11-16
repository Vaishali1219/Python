##matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] 
##  
### Nested List Comprehension to flatten a given 2-D matrix 
##flatten_matrix = [val for sublist in matrix for val in sublist] 
##  
##print(flatten_matrix) 
res = {}
d = [1 , 5 , 9, 12, 19, 2, 8, 13, 18]
c = d.copy()
c.sort(reverse = True) # 19 18 13 12 9 8 5 2 1
res = {j : c[i] for i in range(len(c)) for j in range(len(c)) if c[i] == d[j] if j not in res}
print(res)

    
##def findIndex(c, d):
##    res = {}
##    for i in range(len(c)):
##        for j in range(len(c)):
##            if c[i] == d[j]:
##                if j not in res:
##                    res[j] = d[j]
##    return res

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

    if sum(f.values()) == sum(t.values()):
        a = min(f.keys(), key = (lambda k: f[k]))
        b = min(t.keys(), key = (lambda k: t[k]))
        if f[a] > t[b]:
            return f
        else:
            return t
    else:
        return f
