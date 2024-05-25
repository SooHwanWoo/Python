import os
import pickle

filename = 'score.bin'

class Score:
    def __init__(self, pscore, average):
        self.__pscore= pscore
        self.__average = average

    def display(self):
        return (f'개인 점수: {self.__pscore}\n평균: {self.__average}')
    
def save_file(score):
    with open(filename, 'wb') as file:
        pickle.dump(score, file)

def load_file():
    with open(filename, 'rb') as file:
        s = pickle.load(file)
    return s

def input_scores(lst):
    num = 1
    while True:
        score = int(input(f'#{num}? '))
        if score < 0:
            break
        else:
            lst.append(score)
            num += 1
            
def get_average(lst):
    sumScores = 0
    for i in range(len(lst)):
         sumScores += lst[i]
    return (sumScores/len(lst))

def show_scores(lst):
    x = ''
    for i in range(len(lst)):
        x += f'{lst[i]} '
    return x

if os.path.exists(filename):
    s = load_file()
    print('[파일 읽기]\n\n[점수 출력]')
    print(s.display())
else:
    print('[점수 입력]')
    scores = []
    input_scores(scores)

    print('[점수 출력]')
    print('개인 점수:', end='')
    print(show_scores(scores))
    print(f'평균: {get_average(scores):.1f}')
    a = f'{show_scores(scores)}'
    b = f'{get_average(scores):.1f}'
    save_file(Score(a,b))
