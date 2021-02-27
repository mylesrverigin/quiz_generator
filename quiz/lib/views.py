from quiz import app
from flask import render_template,request,url_for,redirect
import pandas as pd
from quiz.lib.data_fetch import DataFetch
from quiz.lib.question_generator import QuestionGenerator

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz/')
def quiz():
    datafetch = DataFetch(app.config['PATH'])
    names = datafetch.get_file_names()
    question_generator = QuestionGenerator()
    names_to_use = question_generator.file_randomizer(names)
    data = datafetch.get_file(names_to_use)
    question_generator.add_data(data)
    questions = question_generator.run()
    return render_template('quiz.html',questions=questions)