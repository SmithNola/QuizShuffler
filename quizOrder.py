import random

print('How many questions will your quiz have?')
num=input()#retrieves the number of question there are going to be
num=int(num)
quiz={}#will save the quiz

#retrieves quiz questions and answers
for i in range (num):
    print('Enter Question '+ str(i+1))
    question=input()
    quiz[question]=""#inserts the question into the dictionary
    print('How many choices')
    choices=input()
    answers=[]
    choices=int(choices)
    for x in range(choices):#enters each question choice into a list
        print ('Enter choice '+str(x+1))
        answer=input()
        answers.append(answer)
    quiz[question]=answers#enters the choices with their question

quizr={}
mix = list(quiz.keys())
random.shuffle(mix)#mixes up the questions
quizFile=open('quiz%s.txt' % (num), 'w')
quizFile.write('Name:\n\nDate:\n\nPeriod:\n')
for key in mix:
    s=quiz[key]
    random.shuffle(s)#mixes up the answers
    quizFile.write('\n' +str(num)+"." + key)#writes out the question
    for i in s:
        quizFile.write('\n' + i)#writes out the choices

quizFile.close()
