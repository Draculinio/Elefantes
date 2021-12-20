def fibo(n):
    if n<0:
        raise ValueError('Solo nrs positivos')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        nm1 = 1
        nm2 = 0
        for i in range(2,n):
            sum = nm1 + nm2
            nm2 = nm1
            nm1 = sum
        return nm1

print(fibo(1000000))

#SUMO NM1 + NM2
#NM2 = NM1
#NM1 = SUMA