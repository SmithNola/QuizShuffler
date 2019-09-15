import random
print('How many quizes do you need?')
quizes=int(input())
print('How many questions will your quiz have?')
num=input()#retrieves the number of question there are going to be
num=int(num)
quiz={}#will save the quiz

for i in range(num):
    print('Enter Question ' + str(i + 1))
    question = input()
    quiz[question] = ""  # inserts the question into the dictionary
    print('How many choices')
    choices = input()
    answers = []
    choices = int(choices)
    for x in range(choices):  # enters each question choice into a list
        print('Enter choice ' + str(x + 1))
        answer = input()
        answers.append(answer)
    quiz[question] = answers  # enters the choices with their question

for q in range (quizes):
    quizFile=open('quiz%s.txt' % (q+1), 'w')
    #retrieves quiz questions and answers

    quizr={}
    mix = list(quiz.keys())
    random.shuffle(mix)#mixes up the questions
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n')
    for key in mix:
        num=1
        s=quiz[key]
        random.shuffle(s)#mixes up the answers
        quizFile.write('\n' +str(num)+"." + key)#writes out the question
        for i in s:
            quizFile.write('\n' + i)#writes out the choices
        num=num+1

quizFile.close()