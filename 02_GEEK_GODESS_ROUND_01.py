##gqtrawq

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    count = 0
    jud = {}
    test = True
    p=[]
    while test == True:
        T = int(input())
        if T > 0 and T < 11:
            test = False

    V = 0
    while V < T:
        while test == False:
            N = input()
            S = list(N)
#            print(S)
            if len(S) > 0 and len(S) <= 100000:
                test = True
            B = set(S)
#            print(B)
            for x in B:
                if count <= S.count(x):
                    count = S.count(x)
                    temp = x
            jud[count] = temp
            count = 0
            s = sorted(jud.items(), key=lambda x:x[1], reverse=True)
#            print(s)
#            print(jud)
            p+=(s[0][1])
#            print(p)
            V += 1
            s = []
            jud={}
            count = 0
        test = False

    for x in p:
        print(x)

main()















#count = 0
#jud = {}
#test = True
#p=[]
#while test == True:
#    T = int(input())
#    if T > 0 and T < 11:
#        test = False
#
#V = 0
#while V < T:
#    while test == False:
#        S = input()
#        if len(S) > 0 and len(S) <= 100000:
#            test = True
#        for j in S:
#            for k in S:
#                if j == k:
#                    count +=1
#                if j not in jud:
#                    x =ord(j)
#                    jud[x] = count
#            count = 0
#        s = sorted(jud.items(), key=lambda x:x[1], reverse=True)
#        p.append(chr(s[0][0]))
#        V += 1
#    s = []
#    jud={}
#    count = 0
#    test = False
#
#for x in p:
#    print(x)
#        