# 0 1 1 2 3 5 8 13 21 34...
#f0 = 0
#f1 = 1
#fn = fn-1 + fn-2

def fibo(n):
    if n<0:
        raise ValueError('Solo nrs positivos')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        s = [0,1]
        for i in range(2,n):
            s.append(s[i-1]+s[i-2])
        #return s
        return s[-1]

print(fibo(10))
 