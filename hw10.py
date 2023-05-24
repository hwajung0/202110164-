import pickle
import os

filepath='data/score.bin'

def save_data(scores):
    with open(filepath,'wb') as file:
        pickle.dump(scores,file)

def load_data():
    with open(filepath,'rb') as file:
        sc=pickle.load(file)
        print('[파일 읽기]\n')

        print('개인점수:',end='')
        show_scores(sc)

        avg=get_average(sc)
        print(f'평균: {avg:.1f}')
        save_data(sc)


def input_scores():
    s=[]
    i=1
    while (True):
        n=int(input(f'#{i}?'))
        if n<0:
            break
        s.append(n)
        i+=1
    return s
        
def get_average(s):
    total=0
    for n in s:
        total +=n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

if os.path.exists(filepath):
    load_data()
    
else:
    print('\n[점수 입력]')
    scores=input_scores()

    print('\n[점수 출력]')
    print('개인점수:',end='')
    show_scores(scores)

    avg=get_average(scores)
    print(f'평균: {avg:.1f}')
    save_data(scores)






    