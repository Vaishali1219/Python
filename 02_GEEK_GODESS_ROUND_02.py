def fact(n):
    f = 1
    for j in range(1, (n+1)):
        f*=j
    return f

def main():
    test = True
    res = []
    while test==True:
        T = int(input())
        if T>0 and T<11:
            test=False

    V = 0
    while V<T:
        while test==False:
            R = [int(x) for x in input().split() [:2]]
            if R[0] !=0:
                if ((R[0]>0 and R[0]<1001) and (R[1]>0 and R[1]<(R[0]+1))):
                    test = True
                else:
                    test = False

            S = R[0]
            mini = int((S//2))+1
            maxi = S
            max_fact = fact(S)
            suma = 0
##            print('min = {}, max = {}, S = {}, max_fact ={}'.format(mini, maxi, S, max_fact))
            for i in range(mini, maxi):
                min_fact=fact(i)
##                print('min_fact = {}'.format(min_fact))
                if (S%2 == 0):
                    number = int(((max_fact//min_fact)//2))
                else:
                    if (i%2==0):
                        number = ((int(((max_fact//min_fact))-1) // 2)+1)
                    else:
                        number = int(((max_fact//min_fact)//2))
                                  
                suma+=number
##                print('number = {}'.format(number))
            suma+=1
        V+=1
##        print('sum = {}'.format(suma))
        R = []
        res.append(int(suma))
        test = False

    for i in res:
        print(i)

main()
