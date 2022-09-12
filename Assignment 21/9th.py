def table(num,N):
     if N>0:
        table(num,N-1)
        print(num," X ",N," = ",num*N)

table(10,100)