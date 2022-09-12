set={11,22,45.72,True,(3+7j),'MySirG'}
it=iter(set)
while True:
    try:
        print(next(it),end=' ')
    except:
        break