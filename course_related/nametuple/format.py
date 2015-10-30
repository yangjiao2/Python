## want to look pretty
def collection_str(lst: 'list of student') -> str:
    ''' better to look the list of student
    '''
    goodformat = ''
    for a_student in lst:
        goodformat += '{:8}  {:20}  {}  {:2}\n'.format(a_student.ID, a_student.answers, a_student.scores, a_student.total)
    return goodformat
## 



# d multiple-choice test


NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D
CHOICE = ['A', 'B', 'C', 'D']

# d.1
print ('d.1')
from random import *
def random_answers()-> str:
    '''generates and returns a string of letters representing the correct answers to the test.
    '''
    answerStr = ''
    for i in range(NUMBER_OF_QUESTIONS):
        answerStr += choice(CHOICE)
       
    return answerStr
# print (random_answers())
ANSWERS = random_answers()

print ('\nd.2 & d.3')

def scores(ans:str) -> list:
    '''generate the score list for each student
    '''
    scoreList = []
    for i in range(20):
        if ans[i] == ANSWERS[i]:
            scoreList.append(1)
        else:
            scoreList.append(0)
    return scoreList

def total_scores(lst:list)-> int:
    return (sum (lst))
            

from collections import namedtuple
Student = namedtuple('Student', 'ID answers scores total')

def random_students() -> list:
    '''generate and return a list of Student namedtuples
    '''
    list_of_students = []
    for i in range(NUMBER_OF_STUDENTS):
        id_number = randint(10000000, 99999999)
        
        random_answer_for_a_student = random_answers()
        list_of_students.append(Student(id_number, random_answer_for_a_student, scores(random_answer_for_a_student), total_scores(scores(random_answer_for_a_student)) ))
    return list_of_students

#print (random_students())
ALLSTUDENTS = random_students()
#print (ALLSTUDENTS[0].total)

def score_sort(a_student: 'student')-> int:
    '''return the total score for sort function
    '''
    return a_student.total


def top10_and_mean(lst:'list of Student') -> str:
    ''' print top 10 student and the average score
    '''
    lst.sort(key = score_sort, reverse = True)
    average = 0
    
    for a_student in lst:
        average += score_sort(a_student)
    
    print ('The top 10 students are:\n' + collection_str(lst[:10]))
    print ('The average score is', average / NUMBER_OF_STUDENTS)
    
top10_and_mean(ALLSTUDENTS)


# a conventional way to score multiple-choice exams.
print ('\nd.4')

# add to the group of answer choices 0 and twice the number of choices number of correct answer


def random_answers()-> str:
    '''generates and returns a string of letters representing the correct answers to the test.
    '''
    answerStr = ''
    for i in range(NUMBER_OF_QUESTIONS):
        answerStr += choice(CHOICE)
       
    return answerStr
# print (random_answers())
ANSWERS2 = random_answers()

def scores2(ans:str) -> list:
    '''generate the score list for each student
    '''
    scoreList = []
    for i in range(20):
        if ans[i] == ANSWERS2[i]:
            scoreList.append(1)
        else:
            scoreList.append(0)
    return scoreList

def generate_weighted_student_answer(answer_char:str) ->str:
    '''takes a string (one character, the correct answer) and returns a string (one character, the student answer chosen randomly from the enhanced group)
    '''
    CHOICE = ['A', 'B', 'C', 'D']
    copies = randint(0, NUMBER_OF_CHOICES * 2)
    CHOICE.extend(copies * [answer_char])
    #print ('CHOICE', CHOICE)
    weighted_choice = choice(CHOICE)
    return weighted_choice

def random_students2()-> list:
    '''generate and return a list of Student namedtuples
    '''
    list_of_students2 = []

    for i in range(NUMBER_OF_STUDENTS):
        student_answer = ''
        id_number2 = randint(10000000, 99999999)
        for ans in (ANSWERS2):
            student_answer += generate_weighted_student_answer(ans)

        list_of_students2.append(Student(id_number2, student_answer, scores2(student_answer), total_scores(scores2(student_answer)) ))

    return list_of_students2

#print (random_students2())
ALLSTUDENTS2 = random_students2()

top10_and_mean(ALLSTUDENTS2)



print ('\nd.5')
# An unconventional way : assign different weights to different questions
# The questions that were harder (i.e., that fewer people answered correctly) are worth more points than the easier ones.

# assign a number of points to each problem equal to the number of students who missed the problem

def incorrect_number_for_a_question(lst: 'list of Student', i:int) -> int:
    '''counts the number of wrong answers to a single question'''
    total_incorrect_number = 0
    for a_student in lst:
        total_incorrect_number += a_student.scores[i]
    
    return total_incorrect_number
    
def question_weights(lst: 'list of Student') -> 'list of numbers':
    '''takes a list of Student records and returns a list of numbers
    '''
    incorrectList = []
    for i in range(NUMBER_OF_QUESTIONS):
        incorrectList.append(incorrect_number_for_a_question(lst, i))
        #print (incorrect_number_for_a_question(lst, i))
    return incorrectList
    
#print (question_weights(ALLSTUDENTS))
QUESTION_WEIGHTS = question_weights(ALLSTUDENTS2)

def Student_weighted_score(a_student:'a Student reccord', QW: 'list of question weights') ->'Student record':
    '''takes a Student record (and uses the list of question weights you just defined) and returns that Student record with its total field changed to reflect that student's score based on his or her correct answers and the corresponding question weights. 
    '''
    new_scores = []
    for i in range(len(a_student.scores)):
        new_scores.append(a_student.scores[i] * QW[i])
    return Student(a_student.ID, a_student.answers, new_scores, sum(new_scores))

# apply Student_weighted_score
ALLSTUDENTS3 = []
for a_student in ALLSTUDENTS2:
    ALLSTUDENTS3.append(Student_weighted_score(a_student, QUESTION_WEIGHTS))
    
# sort, mean
top10_and_mean(ALLSTUDENTS3)