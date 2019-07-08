# -*- coding: utf-8 -*-

from flask import Flask,render_template,url_for
from flask_bootstrap import Bootstrap
#from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
import subprocess #used to execute linux command in Python env.
from subprocess import Popen, PIPE
from subprocess import check_output



app=Flask(__name__)
#adding bootstrap to our web app
Bootstrap(app)
#for including a database
'''

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///test.db"
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)


import subprocess #used to execute linux command in Python env.
out = subprocess.Popen(['lt-proc', '/home/arushi/new_hnd_mo/mydata'],
           stdout=subprocess.PIPE,
           stderr=subprocess.STDOUT)
'''

#to use form object
app.config['SECRET_KEY']='Thisisasecret'
class EnterText(FlaskForm):
    sentence=StringField('sentence')

#create index route

@app.route('/',methods=['GET','POST'])



def index():
    form=EnterText()
    if form.validate_on_submit():
        with open("/home/arushi/PycharmProjects/mlpackage01/str_test", 'w') as f:
            f.write(form.sentence.data.encode('utf-8'))
            f.close()

        return "<h1>The sentence is {}".format(form.sentence.data.encode('utf-8'))
    return render_template('index.html',form=form)





def get_shell_script_output_using_communicate():
    session = subprocess.Popen(['/home/arushi/PycharmProjects/mlpackage01/doMorphAnal.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')





if __name__=="__main__":
    app.run(debug=True)