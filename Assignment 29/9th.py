import pickle
BookData={'C language':'404','C++':'500','DSA':'300','Python':'200','Java':'350.55'}
f=open('bookfile.txt','wt')
pickle.dump(BookData,f)
f.close()
