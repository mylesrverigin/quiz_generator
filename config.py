class config(object):
    PORT = 5000

class development(config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    PATH = 'C:\code\ericka_quiz\data'
    QUIZ_LEN = 10
    QUESTION_COL = ['Muscle','Action']
    ANSWER_COL = {'Muscle':['Origin','Insertion','Action','Innervation'],'Action':['Muscle','Origin']}