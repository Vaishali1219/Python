a = [1, 2, 12, 13, 25] ##38
sums = []
for j in range(len(a)):
    temp = str(a[j])
    total = a[j]
    for i in range(len(a)):
        for k in range(len(temp)):
            if i == j:
                continue
            elif temp[k] in str(a[i]):
                continue
            else:
                total += a[i]
    sums.append(total)
print(max(sums))
            

    
    
