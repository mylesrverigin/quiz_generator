from flask import Flask

app = Flask(__name__)
app.config.from_object('config.development')

from quiz.lib import views