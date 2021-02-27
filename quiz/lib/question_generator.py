import pandas as pd
import numpy as np
from quiz import app

class QuestionGenerator():
    def __init__(self):
        pass
        
    def run(self):
        return [self.create_question() for i in range(0,self.quiz_len)]

    def add_data(self,data):
        self.data = data
        self.quiz_len = app.config['QUIZ_LEN']
        self.data_len = len(self.data)
        self.question_cols = app.config['QUESTION_COL']
        self.answer_cols = app.config['ANSWER_COL']

    def create_question(self):
        """
        Creates a question based on config answer and question columns using self.data
        """
        row_int = self.randint(self.data_len)
        question_col = self.question_cols[self.randint(len(self.question_cols))]
        answer_col = self.answer_cols[question_col][self.randint(len(self.answer_cols[question_col]))]
        question = self.data[question_col].iloc[row_int]
        answer = self.data[answer_col].iloc[row_int]
        final_question = f'what is the {answer_col} of {question_col} : {question}'
        return (final_question,answer)

    def file_randomizer(self,names,files_to_use=3):
        """
        Takes in a list of file names and an int 
        gives back a list with that many file names
        """
        names_to_use = []
        for i in range(0,files_to_use):
            random_int = self.randint(len(names))
            name = names[random_int]
            if name not in names_to_use:
                names_to_use.append(name)
            else:
                try:
                    name = names_to_use[(random_int-1)]
                    if name not in names_to_use:
                        names_to_use.append(name)
                except:
                    continue
        return names_to_use


    def randint(self,max):
        return np.random.randint(0,max)