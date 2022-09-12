import random
from colorama import Fore
words=['RAEHTF','KABRE','OURITNE','RANEG','OAERELANP','STEILN','AWS','TAC','PSEICAL',
       'EUTIBLUF','DEWNORULF','RYROS','UTHS','YCR','LEBM','PEESHC','LUBHS']

words_form={'RAEHTF':'father','KABRE':'break','OURITNE':'routine','RANEG':'range',
    'OAERELANP':'aeroplane','STEILN':'listen','AWS':'saw','TAC':'cat',
    'PSEICAL':'special','EUTIBLUF':'beautiful','DEWNORULF':'wonderful','RYROS':'sorry',
    'UTHS':'shut','YCR':'cry','LEBM':'blem','PEESHC':'speech','LUBHS':'blush'}
msg=['Arrange the letters to form a valid word:','\nCorrect\n','\nWrong\n','Net Score is']
while True:
    range=set()
    range.clear()
    while len(range)!=5:
        range.add(random.randint(0,16))
    range=list(range)
    i=0
    score=0
    while i<5:
        print(Fore.GREEN+msg[0])
        print(Fore.WHITE+words[range[i]])
        ans=input().lower()
        if(ans==words_form[words[range[i]]]):
            print(msg[1])
            score+=1
        else:
            print(msg[2])
            if score!=0:
                score-=1
        i+=1
    else:
        print(msg[3],score)
    choice=input('If u wants to play again then Press Y/N:')
    if choice=='y' or choice=='Y':
        print()
    else:
        break


     